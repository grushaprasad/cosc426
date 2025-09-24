# COSC 426 F25 Lab 4

## Introduction

In this lab you will build and evaluate bigram language models. 


## Part 1: Practice computing bigram probabilities

In this part, you will manually compute bigram probabilities as a way of reviewing the relevant concepts. 

You will be working with a vocabulary with 8 words. 

```
vocab = {a, the, is, in, likes, eats, sandwich, panda, joyfully, peacefully}
```

#### Part 1.1: MLE bigram probabilities without special tokens

Consider a bigram model that uses `vocab` and is trained on `text` (below):

```
text = ['the panda eats the sandwich in her pajamas',
         'a sandwich likes a panda',
         'the sandwich likes her panda in some pajamas']
```

What probability would this model assign to the following bigrams: 

- `(the, panda)`
- `(a, sandwich)`
- `(in, the)`
- `(panda, eats)`


#### Part 1.2: MLE bigram probabilities with special tokens

Consider a bigram model that has three additional special tokens in its vocabulary, apart from all the words the `vocab`. 

1. `[UNK]` which represents unknown words (i.e. words not in the vocabulary)

2.  `[BOS]` which indicates the start of a sentence

3.  `[EOS]` which indicates the end of a sentence

What probability would the model with the new vocabulary asssign to the the following bigrams?

- `([BOS], the)`
- `([UNK], panda)`
- `(likes, [UNK])`
- `([UNK], peacefully)`
- `([UNK], [UNK])`
- `(panda, [EOS])`
- `(likes, sandwich)`


Also answer the following questions: 


1. Why is it useful to have `[BOS]` and `[EOS]` tokens?
2. Why is it a useful strategy to replace words not in the vocabulary with the `[UNK]` token? 


#### Part 1.3: add-1 bigram probabilities with special tokens

Consider a bigram model that has the same vocabulary as the model in Part 1.2, but uses add-1 smoothing. 

What probability would this new model assign to the following bigrams? 

- `(the, panda)`
- `(a, sandwich)`
- `(in, the)`
- `(panda, eats)`
- `([BOS], the)`
- `([UNK], [UNK])`
- `(panda, [EOS])`

Also answer the following questions: 

1. What is the motivation for smoothing? If it is easier to articulate your answer, describe a scenario where the absence of smoothing is a problem. 
2. What happens to the probability of observed bigrams with smoothing? 
3. Which of the following smoothing types will be closest to the MLE estimate (i.e., unsmoothed estimate) for observed bigrams? `add-1`, `add-2`, `add-0.1`?
4. If the data that you are testing on is very similar to the data used to train your bigram model, would you want to use higher or lower values of `k` in `add-k` smoothing? Why? 


## Part 2: Writing code to compute bigram probabilities

In this part you will write code to get the probability of any bigram `(word1, word2)` given some `text`. Implement the following functions in `Lab4.py`

- `getVocab()`
- `preprocess()`
- `getBigramFreqs()`
- `getBigramProb()`


Some efficiency criteria:

*  `getBigramFreqs` should scale linearly with the total number of bigrams in the text (i.e., time complexity is O(n))
*  `getBigramProb` should run in constant time (i.e., time complexity is O(1))

Make sure to test the code against the test cases provided in the docstrings and doctests. 

## Part 3: Training and evaluating bigram models

In this part, you will train and evaluate bigram models on larger texts. 

1. Write a function in `Lab4.py` that can help you evaluate a given bigram model on some text. 

2. Train a add-1 bigram model on `through_the_looking_glass.txt` 

3. Evaluate your trained model on `through_the_looking_glass.txt`, `alice_in_wonderland.txt` and `sherlock_holmes.txt`. What do you observe? Does this make sense? 

You should implement steps 2 and 3 in `Lab4.ipynb`. 

## Part 4 (Optional): Finding an optimal model  

The bigram model that you've built currently has two hyperparameters (i.e., design choices made by the experimenter): 

* The `k` in `add-k` smoothing
* The choice of whether or not to mark the ends

Lets say you can set `k` to be some value between `0.00001` and `2`. 

1. Systematically vary these hyperparamters in `Lab4.ipynb` to find the best bigram model for `through_the_looking_glass`. 

2. Evaluate your best model on `alice_in_wonderland.txt` and `sherlock_holmes.txt`. Are you convinced that the model you picked is also the best for these two texts? 

3. Based on your answer to the previous question, explain why it is necessary to have three different datasets: train (to train the model), validation (to find the best hyperparameters), test (to evaluate the final model)






