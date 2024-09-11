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

This lab has three parts: 

1. Go from linguistic phenomenon to model evaluation 
2. Systematize your evaluation 
3. Analyze results and compile your findings

## Provided files

-  Lab2.py
- `sample_results.tsv`
- [A google doc
  template](https://docs.google.com/document/d/1kBff1UjvVXto0X-gH4Icb3MbB9zhND0PRCj-c1nz6m4/edit?usp=sharing)
    to write responses
- [A google sheet template](https://docs.google.com/spreadsheets/d/1s_1Fr44kCERzN-c5hK0KnaD8wkTWdPn7Bm0HF03LDuA/edit?usp=sharing)
    to structure Part 1

## What to submit
- Lab2.py
- A **tsv** of your data and results from Part 1
- A **pdf** of the google doc template with your answers

## Part 0

Before starting each lab, get the latest version of the `NLPScholar` repo by
first navigating to the folder on terminal and then executing: 

        git pull

Additionally, a package is missing that you need for today. With the nlp
environment activated run: 

        pip install seaborn

## Part 1: Ideation (60 minutes)

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
Our research question today is **Do transformer-based language models learn
implicit causality?** We will narrow this to a sub-question: **Does distilgpt2
learn the implicit causality bias of verbs?** Your tasks in this lab is to
answer this question. 

In this first part, think through with your group how can answer this question
using the toolkit. Here's some things to keep in mind to help get you started: 

- We can't ask what distilgpt2 thinks a pronoun refers to. We need some
  dependent measure. 
- Can we make examples 1 and 2 into templates? Consider what else we could vary
  to help us see whether the model prefers subject or object referring pronouns.  
- What if we varied the stereotypical gender of the subject and object in a
    sentence? Could we construct meaningful minimal pairs with a pronoun
    uniquely referring to either the subject or the object?  
- distilgpt2 is a causal language model with the name `distilbert/distilgpt2` on
    HuggingFace. Try out some sentences using `interact` to see if you can use
    probability as a depedent measure. 
- Examples of each type of verb are included below. 

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


In this part, you should use the `interact` mode to test some initial ideas for
how to evaluate the model's knowledge. To help scaffold you here, consider this
google
[sheet](https://docs.google.com/spreadsheets/d/1s_1Fr44kCERzN-c5hK0KnaD8wkTWdPn7Bm0HF03LDuA/edit?usp=sharing).
It includes the format you should use to organize your experiment on the sheet
labeled data. There are columns included to help you think through what
information you should included. See the
[MinimalPairAnalysis](https://github.com/forrestdavis/NLPScholar/blob/main/src/analysis/MinimalPairAnalysis.md)
document for more details on these column names. 

 Using `interact` mode you should fill in the results table with your initial
explorations. You should develop around 8 sentences by the end of this part and
an initial result by aggregating over your results table (in the results sheet)

## Part 2: Scaling up (40 minutes)

By the end of Part 1, you should have developed a sense for a **template** you
could use to test a model's knowledge of implicit causality and some initial
results. In this part, you will scale up your experiments and draw on the
`evaluate` mode. You should add to `Lab2.py` code to generate more data for your
experiment. Sample code is provided showing how to do this for subject-verb
agreement
[here](https://github.com/forrestdavis/NLPScholar/blob/main/src/analysis/analysis_util/create_mp_stims.py).
Build on this existing code. 

Detail your considerations and process as you go in your google doc
(which you'll submit later as a pdf). 

## Part 3: Analysis and Findings (20 minutes)

Conduct your experiment using `NLPScholar`. Use the data you made in Part 2 and
the `analysis` mode.  Collect your results and make sense of them. See the
provided code (which use `sample_results.tsv`) for some examples of plotting
results. Plots can help you make sense of your findings! Include your plots in
your google doc. You should answer the question at the start of this lab.
**Justify your answer based on your results.** Finally, consider any limitations
in your experimental design or approach more generally. 

