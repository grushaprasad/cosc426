# COSC 426 F25 HW3

## Introduction

In this homework you will compare the performance of three different types of language models (bigram model, trigram model, and `distilgpt2`). Concretely, you will train each of these models on  `alice_in_wonderland.txt` and evaluate them on `alice_in_wonderland.txt`, `through_the_looking_glass.txt` and `sherlock_holmes.txt`. You will also discuss the role the tokenizer plays in language modeling. 

This HW has three required parts, and one optional part: 

* Part 1: Train and evaluate bigram and trigram models
* Part 2: Train and evaluate `distilgpt2` model
* Part 3: Reflect on the role of the tokenizer
* Part 4 (optional): Explore the effect of tokenizer on ngram model performance



## Provided files

* `HW3.py` which has some helpful starter functions for preprocessing and computing n-gram frequencies.  

* `HW3.ipynb`, which is where you will include your answers to the questions in all the parts. 

* `data` folder with all of the required files (this is the same folder as in Lab 4)

## Submission instructions

You should submit the following files to gradescope:
* `HW3.ipynb` with answers to questions from all the parts.

* `HW3.py` with added functions to compute n-gram probabilities, and to evaluate LMs. 

* Any config and data files you create for Part 2 (and Part 4 if relevant). 

## Part 1: Train and evaluate bigram and trigram models 

For this part, do the following: 

* In `HW3.py`, make sure you understand what the helper functions are doing, and how you can use them. **Note: unlike in Lab4, where we used `glove_vocab` and `nltk` tokenizers, in this HW we are using the `distilgpt2`'s tokenizer and vocabulary.** 

* In `HW3.py` write functions that will allow you to compute bigram and trigram probabilities with addk smoothing, and evaluate LM performance. 

* In `HW3.ipynb` train bigram and trigram models with `add-0.001` smoothing on `alice_in_wonderland.txt`, and then evaluate them on `alice_in_wonderland.txt`, `through_the_looking_glass.txt` and `sherlock_holmes.txt`. 

* In `HW3.ipynb` compare the generalization performance of your bigram and trigram models. 

* (Optional) Try different smoothing methods and evaluate the impact they have on bigram and trigram generalization performance. **Note: if you are attempting this part, you need to create a validation set. Explain why and describe how you chose to create your validation set**


## Part 2: Evaluate pretrained and trained-from-scratch distilgpt2 models 

For this part, do the following: 

* Train a `distilgpt2` model **from scratch** on `alice_in_wonderland.txt`. 

* Evaluate your trained model on `alice_in_wonderland.txt`, `through_the_looking_glass.txt` and `sherlock_holmes.txt`. That is, for each of these texts, get the `P(word | context)` for every word in the text, and then use the same evaluation metric that you used for bigram and trigram models in the previous part. (*Hint: for the purposes of evaluating a given file, treat all of the sentences in that file as having the same sentid*)

* In `HW3.ipynb` compare the generalization performance of this model to your bigram and trigram models. 

* (Optional): Evaluate the pretrained `distilgpt2` model and a `distilgpt2` model finetuned on `alice_in_wonderland.txt`. Compare the performance of these models to the other models. 


## Part 3: Reflect on the role of tokenizer
For this part, answer the following questions in `HW3.ipynb`: 

In this HW we used the `distilgpt2` tokenizer to tokenize the text for all the langauge models. Explain why we cannot use the nltk tokenizers we used in Lab4 in Part 1, if we want to compare the performance of our bigram and trigram LMs with `distilgpt2` performance.  


## Part 4 (Optional): Explore the effect of tokenizer and vocab on ngram model performance

For this part, you should try at least two other forms of tokenizing text and two other vocabulary choices, and evaluate your bigram and trigram model performance. Concretely, in `HW3.ipynb` you should:

* Describe your tokenizers and vocabulary combinations, and justify why you picked them.  
* Evaluate your trigram and bigram models on your new tokenizer-vocabulary combinations 
* Discuss your results, and describe any insight that you gained about how tokenizer and vocabulary choice might impact language model performance. 

## Grading

### Meets expectation designation

In order to get this designation, you should meet all of the following requirements: 

* Your `HW3.py` correctly implements the functions required to train and evaluate bigram and trigram language models. 

* Your `HW3.ipynb` correctly runs all of the experiments and answers all the questions required for parts 1 and 2. 

* You create and submit correct config and data files for Part 2. 

* Your response to Part 3 demonstrates that you put thought into the question and understand the role the tokenizer plays in LM evaluation. 

* You submit all of the required files. 

### Exceeds expectation designation

In order to get this designation, you should meet at least one of the following requirements: 

* In Part 1, you try a range of different smoothing methods, and include a thoughtful discussion of the impact of the smoothing methods on LM performance. You should also motivate the importance of a development (or validation) split. 

* In Part 2, you evaluate the pretrained and finetuned versions of `distilgpt2` and include a thoughtful disussion of how these results compare to the other LMs you conisdered in the HW. 

* You correctly complete Part 4, and include a thoughtful discussion. 

 

























