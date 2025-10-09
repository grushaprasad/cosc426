import tensorflow as tf
import os
from transformers import BertConfig, BertForSequenceClassification, BertTokenizer
import argparse
import json
import torch
import logging
logger = logging.getLogger(__name__)


def load_tf_weights_in_bert(model, config, tf_checkpoint_path):
    """ Load tf checkpoints in a pytorch model. 
    Function adapted from https://github.com/huggingface/transformers/blob/main/src/transformers/models/bert/convert_bert_original_tf_checkpoint_to_pytorch.py
    """
    try:
        import re
        import numpy as np
        import tensorflow as tf
    except ImportError:
        logger.error("Loading a TensorFlow model in PyTorch, requires TensorFlow to be installed. Please see "
            "https://www.tensorflow.org/install/ for installation instructions.")
        raise
        
    tf_path = os.path.abspath(tf_checkpoint_path)
    logger.info("Converting TensorFlow checkpoint from {}".format(tf_path))
    # Load weights from TF model
    init_vars = tf.train.list_variables(tf_path)
    names = []
    arrays = []
    for name, shape in init_vars:
        logger.info("Loading TF weight {} with shape {}".format(name, shape))
        array = tf.train.load_variable(tf_path, name)
        names.append(name)
        arrays.append(array)

    for name, array in zip(names, arrays):
        if 'bert' not in name: ## i.e. not a BERT parameter; we will load classifier parameters separately
            continue
        name = name.split('/')
        # adam_v and adam_m are variables used in AdamWeightDecayOptimizer to calculated m and v
        # which are not required for using pretrained model
        if any(n in ["adam_v", "adam_m", "global_step"] for n in name):
            logger.info("Skipping {}".format("/".join(name)))
            continue
        pointer = model
        for m_name in name:
            # print(m_name)
            if re.fullmatch(r'[A-Za-z]+_\d+', m_name):
                l = re.split(r'_(\d+)', m_name)
            else:
                l = [m_name]
            if l[0] == 'kernel' or l[0] == 'gamma':
                pointer = getattr(pointer, 'weight')
            elif l[0] == 'output_bias' or l[0] == 'beta':
                pointer = getattr(pointer, 'bias')
            elif l[0] == 'output_weights':
                pointer = getattr(pointer, 'weight')
            elif l[0] == 'squad':
                pointer = getattr(pointer, 'classifier')
            else:
                try:
                    pointer = getattr(pointer, l[0])
                except AttributeError:
                    logger.info("Skipping {}".format("/".join(name)))
                    continue
            if len(l) >= 2:
                num = int(l[1])
                pointer = pointer[num]
        if m_name[-11:] == '_embeddings':
            pointer = getattr(pointer, 'weight')
        elif m_name == 'kernel':
            array = np.transpose(array)
        try:
            assert pointer.shape == array.shape
        except AssertionError as e:
            e.args += (pointer.shape, array.shape)
            raise
        logger.info("Initialize PyTorch weight {}".format(name))
        pointer.data = torch.from_numpy(array).contiguous()
    return model

def convert_mnli_tf_checkpoint(tf_checkpoint, pytorch_dump_path):
    """
    Convert a TF checkpoint to PyTorch using Hugging Face converter.
    """
    
    # 1. Create config
    config = BertConfig.from_pretrained("bert-base-uncased")
    config.num_labels = 3 ## nli has 3 labels
    config.architectures = ["BertForSequenceClassification"]
    print(config)
    
    # 2. Create the model
    model = BertForSequenceClassification(config)
    print(model)
    
    # 3. Map encoder and pooler weights
    model = load_tf_weights_in_bert(model, config, tf_checkpoint)
 
    # 4. Map MNLI head manually
    tf_vars = tf.train.list_variables(tf_checkpoint)
    model.classifier.weight.data = torch.from_numpy(tf.train.load_variable(tf_checkpoint, "output_weights")).contiguous()
    model.classifier.bias.data = torch.from_numpy(tf.train.load_variable(tf_checkpoint, "output_bias")).contiguous()
    
    # 5. Save model
    os.makedirs(pytorch_dump_path, exist_ok=True)
    model.save_pretrained(pytorch_dump_path)
    config.save_pretrained(pytorch_dump_path)

    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    tokenizer.save_pretrained(pytorch_dump_path)

    print(f"Saved PyTorch model to {pytorch_dump_path}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert TF MNLI BERT checkpoint to PyTorch")
    parser.add_argument("--tf_checkpoint", type=str, required=True,
                        help="Path to TensorFlow checkpoint prefix (no extension). Example: /path/to/bert_model.ckpt")
    parser.add_argument("--output_dir", type=str, required=True,
                        help="Directory to save PyTorch model and config")

    args = parser.parse_args()

    convert_mnli_tf_checkpoint(args.tf_checkpoint, args.output_dir)