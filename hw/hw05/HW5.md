# COSC 426 F25 HW5

## Introduction

The goal for this homework is two fold: 

1. Learn to build a neural network langauge model. 

2. Understand how the `train` and `evaluate` modes in NLPScholar work behind the scenes. 

Concretely, you will train and evaluate a LSTM language model on `SAE` and `Yoda` sentences from HW2. Like with the CBOW model from Lab 7, you will be working with four classes:

* `LM_Dataset`: this is the class to load data and is partially implemented; you have to complete parts of this. 

* `LSTM_LM`: this is the model class and is fully implemented; you have to answer questions about how it is implemented.

* `LSTM_Trainer`: this is the fully implemented trainer class. 

* `LSTM_Evaluator`: this is the partially implemented evaluator class that you have to complete. 

This HW has three required parts, and one optional part: 

* Part 1: Understanding and completing the four classes
* Part 2: Generating predictions from models trained on SAE and Yoda sentences
* Part 3: Analyzing and interpreting the predictions with the analyze mode from NLPScholar. 
* Part 4 (optional): Implement a bidirectional version of the LSTM_LM (i.e., build a masked language model)

## Provided files

* `LM.py` which has all the four classes
* `HW5.ipynb`, which is where you will include your answers to the questions in all the parts. 
* `data` folder with the vocab, training, and evaluation files.

## Submission instructions

You should submit the following files to gradescope: 

* `LM.py` with all of the missing parts implemented
* `HW5.ipynb` with answers to questions from all the parts, and cell outputs visible. 
* Any config files that you used for Part 3.
* (Optional) `MaskedLM.py` which has the implementation for the bidirectional model. 

## Part 1: Understanding and completing the four classes

### Part 1.1: LM_Dataset

For this part you should: 

1. In `LM.py`, implement `load_vocab` and `load_text`
2. In `Lab5.ipynb`, test your implementation by creating a dataset object, and adding sanity checks. 
3. In `Lab5.ipynb`, explain how the contexts and targets are specified in `make_pairs`, and how this differs from the `make_pairs` function in the CBOW model both at a conceputal and at an implementational level. 

### Part 1.2: LM_Model

For this part you should answer the following questions in `Lab5.ipynb`

1. Why does the decoder take as input a tensor of nHidden and return tensor of vocabSize? Why does it not have the sequence length (i.e., the number of words in the sequence) as one of the dimensions? 

2. You will notice that the LSTM layer returns more outputs than the Linear layer. What are these additional outputs that this layer generates? Why are they important?

3. What is the purpose of the `init_hidden` function? 

4. Is there any difference in the loss function between the CBOW and LSTM_LM models? Why or why not? 


### Part 1.3: LM_Trainer

For this part, you should answer the following questions in `Lab5.ipynb`. 

1. Compared to the CBOW trainer, there are a couple of additional steps in this trainer. What are these steps? Why are they important?

2. Compared to the CBOW trainer, there is one additional step after the loss is computed. What is this step? Why is this important?

### Part 1.4: LM_Evaluator

For this part you should do the following: 

1. In `Lab5.ipynb` answer the following question: what parts of the `compute_loss` function in this evaluator are different from the CBOW evaluator? 

2. In `Lab5.ipynb` answer the following question: For the CBOW model, to generate the prediction for some input we took the label with the maximum logit value. In the case of langauge modeling why is this not appropriate? What do we actually want to get? 

3. In `LM.py` implement `get_preds` and `save_preds`

## Part 2: Generating predictions from models trained on SAE and Yoda sentences

For this part, you should do the following in `Lab5.ipynb`: 

1. Pick a value for `nEmbed`, `nHidden`, and `nLayers`. Justify your choices. 

2. Train a SAE model using the hyperparameters you picked in 1 with  `sae_train.tsv` and `sae_valid.tsv`. Train it for at least 20 epochs.  

3. Train a Yoda model using the hyperparameters you picked in 1 with  `yoda_train.tsv` and `yoda_valid.tsv`. Train it for at least 20 epochs.  

4. Use the functions you wrote in Part 1.4 to evaluate your two models on `eval.tsv`. This should give you a file that looks identical in format to what NLPScholar would give you if you ran evaluate mode with two models. 

## Part 3: Analyzing and interpreting the predictions with the analyze mode from NLPScholar

For this part, you should run the analyze mode on NLP Scholar on the prediction file you generated to investigate whether the two models learned something during training. In `Lab5.ipynb` answer the following questions: 

1. Which of the outputs of the analyze mode (`by_word`, `by_pair`, `by_cond` did you decide to look at? Why?

2. Do you think SAE and Yoda models learned different things? Why or why not? Present concrete parts of your results in the ipynb cell output, and reference this in your answer. 

## Part 4 (optional): Implement a bidirectional version of the LSTM_LM (i.e., build a masked language model)

For this part you should: 

1. In a new file `MaskedLM.py` implement a bidirectional version of the LSTM model. 

2. In `Lab5.ipynb` answer the following question: do you need to change any other parts of the pipeline? Why or why not? If you said you need to change other parts, make those changes. 

3. Repeat the experiment from Part 2 and 3 on either the Yoda or SAE model (or both!). Do you notice any differences in what the model learned?

## Grading

### Meets expectations

In order to get this designation, you should meet all of the following requirements: 

* You answer all of the code comprehension questions in a manner that clearly articulates your thought process.  

* You implement all of the missing parts in Part 1 and add comments. 

* You train and generate predictions from both SAE and Yoda models for part 2.  

* You correctly use the analyze mode of NLP Scholar for part 3 and include thoughtful answers to the questions. 

* You submit all of the required files. 

### Exceeds expectation designation

In order to get this designation, you should meet the following requirements:

* Your implementation of the bidirectional model is complete enough for you to be able to generate predictions from the model -- i.e., if you have minor errors in the model, but can get the model to generate predictions in the right format, that is ok. If you are unsure about parts of your implementation, you include a discussion.   

* Your answers to the questions demonstrate that you understand the difference between bidirectional and unidirectional LSTMs at a conceptual and implementational level.  










