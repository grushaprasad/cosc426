# COSC 426 F24 Lab 2

## Introduction

The purpose of this lab is to give you hands on experience using the
`NLPScholar` toolkit to answer a question about the linguistic knowledge of a
pre-trained transformer language model. By completing this lab, you will
demonstrate that you can: 

- Develop linguistically motivated evaluation data 
- Apply the NLPScholar toolkit to answer a research question 
- Develop skills in conducting research 

#### Pre-requisites

This lab assumes that you have already cloned the `NLPScholar` repository and
have installed the `nlp` environment by following the instructions in
`Install.md`. 

## Structure

This lab has four parts: 

1. Understand the linguistic phenomenon and research question
2. Describe how you will use the `NLPScholar` toolkit to answer the research question
3. Use the `NLPScholar` toolkit to generate results 
4. Interpret the results 

## Provided files

-  Lab2.py
- `sample_data.tsv`
- [A google doc
  template](https://docs.google.com/document/d/1bFvUQha8hpSYZeKPBZmteAiRXcw2TZwVj6ctI8vER60/edit?usp=sharing)
    to write responses

## What to submit
- Lab2.py
- A **tsv** of your condition data from Part 2.
- (Optional) The modified **Lab2.py** file with the function(s) you used to create your input data (if you modified the file)
- A **tsv** file of your results from Part 3. 
- A **pdf** of the google doc template with your answers.

## Part 0

Before starting each lab, get the latest version of the `NLPScholar` repo by
first navigating to the folder on terminal and then executing: 

        git pull

Additionally, a package is missing that you need for today. With the nlp
environment activated run: 

        pip install seaborn

## Part 1: Understanding the research question and linguistic phenomenon (40 minutes)

Consider the following motivating examples: 

1. Sally frightened Mary because she was so terrifying. 
2. Sally feared Mary because she was so terrifying. 

Technically, the pronoun in both 1 and 2 is ambiguous. However, speakers report
strong preferences for who `she` should refer to in these sentences. Take a
minute to check your judgments. 

The core insight is that speakers prefer `she` to refer to the subject `Sally`
in 1 and the object `Mary` in 2. The sentences are otherwise the same, so it
must be the verbs `frightened` and `feared` which modulate preferences. That is,
these sentences form a **minimal pair** where the main verb (`frightened` or
`feared`) is varied. 

In fact, many (possibly all) languages have verbs like this ([Harshorne et al.,
2013](https://doi.org/10.1027/1618-3169/a000187)). These verbs are called
`implicit causality` verbs. There are two types: `subject implicit causality`
verbs like `frightened` and `object implicit causality` verbs like `feared`.

#### Research question: 
**Do transformer-based language models learn
implicit causality?** We will narrow this to a sub-question: **Does distilgpt2
learn the implicit causality bias of verbs?** Your tasks in this lab is to
answer this question. 

#### Questions to answer: 

1. How could you measure if the model learned implicit causality in the specific example pair above? (i.e., what would be your **dependent measure**)

2. Say you are given a list of verbs (e.g. see table below) which have either a Subject IC bias (like frightened) or an Object IC bias (like feared). How could you measure if the model learned implicit causality for all of the verbs? 

3. The example above has a specific format (or "template"). Can you come up with at least one other template in which you think the model's IC bias might be different (either in direction, or the magnitude of bias)? It might be helpful to think here about what are all the parts of the template you can systematically vary, and why these parts might influence IC bias. 

4. Use the `interact` mode to see if your intuitions about the IC bias for `distilgpt2` in the different templates were correct. Note: distilgpt2 is a causal language model with the name `distilbert/distilgpt2` on HuggingFace. For this part, your exploration does not have to be expansive (e.g., try only a few sentences and verbs, not everything). In your answer, include screenshots of the things you tried, and highlight which specific outputs of the interact were your answers based on. 


| Subject IC | Object IC | 
| ---------  | --------  | 
| frightened | feared |
| bored      | believed  | 
| frustrated | encouraged | 
| betrayed   | cherished | 
| amazed     | blamed   | 
| confused   | divorced | 
| amused     | revered  | 
| worried    | trusted | 
| haunted    | liked  | 
| upset      | valued | 


## Part 2: Describing how to use the toolkit to explore the reasearch question more robustly (40 minutes)

As you might have discovered, while the `interact` mode is helpful to get quick intuitions, it can be tedious if you want to run more robust experiments. In this part, you will work through how you will use the `evaluate` and `analyze` modes to answer the questions. 

The documentation for [the `analyze` mode of the MinimalPairAnalysis experiment](https://github.com/forrestdavis/NLPScholar/blob/main/src/analysis/MinimalPairAnalysis.md) outlines what the format of the data needs to be like. 

Do the following: 

1. Read this documentation and then manually create a table with the columns for TSV file with conditions. For now, just include a couple of minimal pairs. The goal here is for you to understand what each of the columns mean. You can use existing spreadsheet software (e.g., excel, google sheets) for this. 

2. Scale up and create a larger TSV file with at least 3 verbs each in the Subject and Object IC bins, and two templates. It is probably easiest to write a python function that will generate this TSV file (see sample code [here](https://github.com/forrestdavis/NLPScholar/blob/main/results/minimal_pairs.tsv) for a different experimental setup). However, you are also welcome to do this part manually. If you write a function, please add that to your `Lab2.py` file. 

3. Describe how you would use this file to get the final results from the analyze mode. For an example of what the results might look like for a different experimental setup (not with IC verbs) look at this [tsv file](https://github.com/forrestdavis/NLPScholar/blob/main/results/minimal_pairs.tsv).

Note: If you are finding that writing the python file for part 2 is taking you a long time, it can be helpful for you to start by testing to make sure you can work through Part 3 with a small (if imperfect) manually generated file, before trying to perfect your templates. 

## Part 3: Using the toolkit (10 minutes)

Use the toolkit to run the experiment you described in the previous part. You wil submit the file that is outputted by the `analyze` mode. 


## Part 4: Analysis and Findings (20 minutes)

Look at the results file generated by the `analyze` mode and make sense of them. See the
provided code (which use `sample_results.tsv`) for some examples of plotting
results. Plots can help you make sense of your findings! Include your plots in
your google doc. You should answer the question at the start of this lab.
**Justify your answer based on your results.** Finally, consider any limitations
in your experimental design or approach more generally. 


