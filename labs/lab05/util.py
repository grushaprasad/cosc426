import nltk
from transformers import AutoTokenizer


def get_vocab(vocab_fname: str) -> set:
    """
    Args:
        vocab_fname: filepath to vocab file. Each line has a new vocab item

    Returns:
        A set of all the vocabulary items in the file plus three additional tokens:
            - [UNK] : to represent words in the text not in the vocab
            - [BOS] : to represent the beginning of sentences.
            - [EOS] : to represent the end of sentences.
        If you run this function on the glove vocab, it should return set with 400003 items.

    >>> len(getVocab('glove_vocab.txt'))
    400003
    """

    with open(vocab_fname, "r") as f:
        dat = f.read().split("\n")

    dat = set([item.strip() for item in dat if len(item) > 0])
    dat.add("[UNK]")
    dat.add("[BOS]")
    dat.add("[EOS]")
    return dat


def get_hf_vocab(modelname):
    """
    Params:
        modelname: string of hf modelname
    Returns:
        The vocabulary used by the huggingface model

    """
    tokenizer = AutoTokenizer.from_pretrained(modelname)
    return tokenizer.vocab


def hf_tokenize(text: str, kwargs):
    """
    Params:
        text: string of text
        kwargs: dictionary with kwargs. Should include key 'modelname' which specifies the hf modelname
    Returns:


    """
    modelname = kwargs["modelname"]

    tokenizer = AutoTokenizer.from_pretrained(modelname)
    tokenized_output = tokenizer(text)
    words = tokenizer.convert_ids_to_tokens(tokenized_output["input_ids"])
    return words


def nltk_tokenize(text: str, kwargs) -> list:
    """
    Params:
        text: string of text

    Returns:
        text broken down into list of tokens using nltk prebuilt function

    """
    return nltk.word_tokenize(text)
