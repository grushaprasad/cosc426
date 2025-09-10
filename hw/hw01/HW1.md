# COSC 426 F25 HW1

## Introduction

In this homework, you will continue to work on the implicit causality phenomenon from Lab 2. This homework is designed to give you practice with the following skills: 

* Translate ideas/results from human langauge production/comprehesion to hypotheses about language model behavior.  

* Given some hypothesis about language model behavior, templatically create data to systematically test the hypothesis.

* Move beyond toy data and run a moderate sized experiment using NLPScholar.

Concretely, you will replicate at least one result from the following paper: [Implicit causality bias in English: a corpus of 300 verbs](https://link.springer.com/article/10.3758/s13428-010-0023-2). 

You can find the data for required for this lab in the electronic supplementary materials at the end of the paper, also linked [here](https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-010-0023-2/MediaObjects/13428_2010_23_MOESM1_ESM.xlsx) for convenience. 

## Paper summary

In the lab, we stated that certain verbs had either a subject IC or object IC bias in humans. But how do we determine what this bias is? This paper establishes the bias for 300+ verbs in English based on participants' responses on a web-based sentence completion task. They studied how a verb's IC bias (i.e., whether people preferred the first or the second NP) was influenced by factors such as word frequency, semantic category, participants' gender etc. 

Here is a non-comprehensive list of things they found: 

1. Low frequency verbs elicited more NP1 continuations than high frequency verbs.

2. Activity verbs (e.g., kiss) had a weaker bias (towards either NP) than psychological verbs (e.g., love). 

3. Participants' sentence continuation strategy differed significantly between men and women (they only considered binary gender in this paper): women tended to have a bias to pick the first NP, whereas men were more likely to attribute the cause to the male NP, irrespective of whether the male NP was the first or second. 


## Your task 

Your task in this homework is to compare `distilgpt`'s verb bias to human bias in this paper. Concretely, you have to answer at least one of the following questions:

1. How does the model's NP1 bias change with verb frequency? 

2. Do activity verbs have a weaker bias than psychological verbs?

3. Does model bias align more closely with female participants (i.e., always pick first NP) or with male participants (i.e., pick male NP)?

To answer these questions, here are the things you will need to do: 

* Automatically create datasets using simple templates in Python (instead of manually typing out all of the sentences in a spreadsheet)

* Use NLPScholar to compute the bias for every pair. In this assignment, we assume that a minimal pair has an NP1 bias if the probability of NP1 continuation is greater than the probabilty of NP2 continuation. (*Hint: look back at the lab to reason about how you can find the probability of NP1or NP2 continuation*)

* Compute the aggregate bias for each condition. Note: what your condition is depends on what question you pick. (*Hint: depending on how you set up your NLPScholar experiment, you might have to use pandas for this step*) 

* Display the results (i.e., generate a plot or print a table) that directly answer the question(s) that you picked. 


## Submission instructions

You should submit the following files to gradescope: 

* The python file you used to create the dataset
* Your dataset
* Config file(s) you used to run the NLPScholar experiment(s)
* `HW1.ipynb` in which you load in the results from your experiment, display them, and answer the question(s)

## Grading

### Meets expectation designation

In order to get this designation you should meet all of the following requirements:

* Pick one of the three questions 

* Create and submit a dataset with at least 10 verbs and 4 NPs. 

* Submit the python file you used to automatically create your dataset 

* The verbs and NPs that are in the dataset should be appropriate for answering the question that you pick. 

* Submit the appropriate config file you used to run the NLPScholar experiment

* Submit the HW1.ipynb notebook with the answer to your question. 

### Exceeds expectation designation

In order to get this designation, you should meet at least one of the following requirements: 

* You use all of the 300 verbs in the dataset

* You answer more than one question

* You use more than one template and motivate why using the additional template is scientifcally interesting. 


