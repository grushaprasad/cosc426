# COSC 426 F25 HW4

## Introduction

In this homework you will compare two types of `distilgpt` based classifiers: 

* A `distilgpt` based Bayesian Classifier
* A `distilgpt` based Neural Network Classifier (i.e., a `TextClassification` model on NLPScholar)

This HW has three required parts, and one optional part: 

* Part 1: Train and evaluate `distilgpt` based Bayesian Classifier
* Part 2: Train and evaluate `distilgpt` based TextClassification model
* Part 3: Reflect on the two approaches to classification
* Part 4 (optional): Error analysis comparing the two approaches to classification

## Provided files

* `HW4.ipynb`, which is where you will include your answers to the questions in all the parts. 

## Submission instructions

You should submit the following files to gradescope:

* `HW4.ipynb` with answers to questions from all the parts.

* Any python scripts that you used to create appropriately formatted datasets. 

* Any config files that you used. 

## Dataset
You will train these classifiers on the [IMDB sentiment analysis
dataset](https://ai.stanford.edu/~amaas/data/sentiment/) that you worked with in Lab. You should minimally: 
* Train the models on 5000 sentences from the `train` folder (2500 positive, 2500 negative). 
* Evaluate the models on at least 2000 sentences from the `test` folder (1000 positive, 1000 negative)



## Part 1: Train and evaluate a `distilgpt` based Bayesian classifier

In this part, you will train a Bayesian classifier that: 
* Estimates **likelihood** with `distilgpt`
* Uses a uniform **prior** (i.e., equal probabilty to both classes)

Do the following: 

* In `HW4.ipynb` outline the steps you will need to take to train a Bayesian classifier using distilgpt. (*Hint: It might help to think back to how you implemented a unigram bayesian classifier in the lab*)

* Create the required datafiles and config files required to train and evaluate the classifier.

* Train and evaluate your model.  

* In `HW4.ipynb` display and discuss your results

Note: you are working on training and evaluating neural network models on fairly long texts. It is expected that this will take time. Training or evaluating the model on 2500 sentences took about 15-20 minutes on my laptop with gpu. It is probably wise to use Turing for this, and leave yourself enough time! 

## Part 2: Train and evaluate a `distilgpt` based TextClassification model

In this part, you will use the `TextClassification` mode in `NLPScholar`. You should: 

* Create the required datafiles and config files required to train and evaluate the classifier.

* Train and evaluate your model.  

* In `HW4.ipynb` display and discuss your results. Compare your results in this part to the results from Part 1. 

Note: To make this comparison between the two parts fair, you train and evaluation sets should be the same in both parts! 

## Part 3: Reflect on the two approaches to classification

For this part, answer the following question in `HW4.ipynb`: In parts 1 and 2, you used `distilgpt` as a base to built a text classifier. At a conceptual level, what is the difference between these two approaches? 

## Part 4 (Optional): Error analysis comparing the two approaches to classification

For this part, answer the following question: To what extent do the predictions from the Bayesian classifier align with the predictions from the `TextClassification` model? Do both the models make the same kinds of errors? Discuss the similarities and differences.
  

## Grading

### Meets expectations

In order to get this designation, you should meet all of the following requirements: 

* You correctly train the models in both parts on at least 2500 positive and negative sentences each (so 5000 in total) and correctly evaluate the models on at least 2000 sentences. 

* Your `HW4.ipynb` displays and discusses the results from your experiments and includes answers all other questions. 

* Your response to Part 3 demonstrates that you put thought into the question and understand the difference between the two approaches to classification. 

* You submit all of the required files. 

### Exceeds expectation designation

In order to get this designation, you should meet at least one of the following requirements:

* You train and evaluate your model on the entire dataset, and compare the results to training and evaluating on the smaller subset. 

* You correctly complete Part 4, and include a thoughtful discussion.



