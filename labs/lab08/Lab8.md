# COSC 426 F24 Lab 8

## Introduction
In this lab you will build and evaluate a model for token classification.  By
completing this lab, you will demonstrate that you are able to train, evaluate,
and use a token classification model for a real world application. 

## Provided files

- `Lab8.py`
- [A google doc template](https://docs.google.com/document/d/10mEZ7KSOXFET4InTg7b4kUK9dTxn_h9KC7I_jX3S11o/edit?usp=sharing)

## What to submit
- `Lab8.py` 
- config files from Part 2 and Part 3. 
- A pdf of your google doc


## Part 0: Setting Up

Pull the most recent version of `NLPScholar` using `git pull`. 

## Part 1: Our Goal (across the lab and the homework)

Our broad goal across the homework and the lab is to build a prototype news
search engine. To build this, we will use the Named Entity Recognition (NER) task. As a motivating example for NER, consider the following text: 

`while eating an apple, the founder of apple thought of a logo in san francisco`

We'd like to be able to label this text with labels, like that the second apple and not the first apple is an organization and that san francisco is a location. That way, people can search for the organization apple and return only those articles about the corporation and not the food, for example. 

In the lab, we will train a model, a NER model, that labels
news text with their tags. We can use these tags to extract phrases which we call entities. In the homework, we will use our trained model to build a small search engine over news data. 

For training our model we will use the data in `ner_news_data`. For using our trained model for search, we will use the data in `news_data`. These folders include information about the data. Please review this. 

**Question 1**: What is the difference between `ner_news_data` and `news_data`? Why do we need data in different formats for training vs. searching? 

**Question 2**: Sketch out the task of the **lab**. What will you do? What data
will you use? What will your functions do? 

**Question 3**: Sketch out the task of the **hw**. What will you do? What data
will you use? What will your functions do? 

Note: `Lab8.py` includes functions with docstrings that will help scaffold your
approach. **Please review these and follow up with your instructor prior to
continuing on.**

## Part 2: Training an NER Model 

In this part, you will train the NER model you will use in the homework. Data is provided in the `ner_news_data` folder. You should formulate a config file that trains `bert-base-cased` for one epoch on token classification. Please review the following folder on NLPScholar for an example of training an token
classification model on part-of-speech tagging:
[link](https://github.com/forrestdavis/NLPScholar/tree/main/src/docs/token_classification_example). **You will submit this config file**.

## Part 3: Extracting Entities

In this part, you will use your trained NER model to extract entities from some
news data. For that, we need to accomplish two things

1. Formatting our test data in the format needed for `evaluate` mode with `TokenClassification`

2. Extracting three types of entities from the text. 

For 2, we are focusing on three tags, `LOC` for location, `ORG` for
organization, and `PER` for person. Notice that tags come with an initial bit of information, `B`, `I`, `L`, `U`. These mean beginning, inside, last, or unit,
respectively. Consider the following illustrative example of predicted tags to
help understand our goal (the tags aren't necessarily correct, just trying to
give a motivating example): 

|  Word     | Tag     | 
| ----- | ---- |
| Bill  | U-Per|
| Peter  | U-Per|
| and   | O    | 
| Melinda | B-Per |
| Gates   | L-Per |
| went    | O     | 
| to      | O     | 
| visit   | O     | 
| Orlando | B-LOC |
| Disney  | B-ORG | 
| World   | I-ORG | 
| Saratoga | B-LOC | 
| Springs  | L-ORG |


We would extract entities PER: ['Bill', 'Peter', 'Melinda Gates'], LOC: ['Orlando',
'Saratoga'], and ORG: ['Disney World', 'Springs']. Note, how U yields an entity
immediately, and how B/I/L are or are not referenced/used.

You will submit your evaluation config file and `Lab8.py` which contains the
functions you need. 
