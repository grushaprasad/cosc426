# COSC 426 F25 Lab 2

## Introduction

The goal of this lab is to practice applying the MinimalPair paradigm to a concrete linguistic phenomenon. There are four parts. 

* Part 1: Understanding the phenomenon
* Part 2: Use NLPScholar to answer concrete questions.
* Part 3: Reflection about how to extend this (which will be useful for HW1)

## Submission instructions

* `Lab2.ipynb` with answers to all of the questions in all the parts. **Make sure that when you submit the file, the outputs in the cells are visible on gradescope.** 

* TSV and config files you created for part 2

**If you work in a group, one member of the group should create a submission on gradescope and add the others to the submission**


## Part 0: Update NLPScholar

Get the most recent version of NLPScholar by going into the directory and typing: 

`git pull`


## Part 1: Understanding implicit causality

Consider the following motivating examples: 

1. Sally frightened Mary because she was so terrifying
2. Sally feared Mary because she was so terrifying

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


### Research question: 
**Do transformer-based language models learn
the implicit causality verb-biases?** We will narrow this to a sub-question: **Does distilgpt2
learn the implicit causality bias of verbs?** Your tasks in this lab is to answer this question. 

Note: `distilbert/distilgpt2` is a causal langauge model, which means that it only conditions on the left context. 

### Questions to answer

Answer the following questions, and verify the answer with me before moving on to the next part. 

**Remember: This might be the first time you are tackling these types of questions. Don't be disheartened if it takes you time to think through this!**


1. At a high level, how can you evaluate whether `distilbert/distilgpt2` has the same implicit causality bias as you for the verb `frightened`? Come up with a minimal pair, and describe how you want to use the minimal pair. Some hints: 
    * You do not have to be constrained by the specific example sentence above -- feel free to modify it as you think is appropriate.
    * Think about how the fact that `distilbert/distilgpt2` is **a causal language model** impacts your approach.  

2. In the minimal pair you came up with, what is/are target word(s) in the minimal pair you should look at?  

3. In the minimal pair you came up with, which is the "expected" sentence and which is the "unexpected"? Why? 



## Part 2: Generating the appropriate TSV file

For this lab, you will be working with the following four verbs, where Subject IC verbs have a bias to refer to the subject NP, whereas Object IC verbs have a bias to refer to the object NP.  

| Subject IC | Object IC | 
| ---------  | --------  | 
| frightened | feared    |
| bored      | believed  | 

You will use NLPScholar to answer the following questions: 

1. Does `distilbert/distilgpt2` learn the subject IC verb bias for `frightened` and `bored`? 

2. Does `distilbert/distilgpt2` learn the object IC verb bias for `feared` and `believed`?

### Part 2.1 Generate the dataset

Generate the TSV file you will use with NLPScholar. You can either create this in a text file, or use a spreadsheet (e.g., google sheets, excel, or numbers) and export it to the TSV format. **Check-in with me before moving on to the next part.**

### Part 2.2 Run NLPScholar

Create the appropriate config file to run the experiment on NLPScholar, and then run it. 

### Part 2.3 Report the results in Lab2.ipynb 

Load the data, and display the results necessary to answer each of the questions. 


## Part 3: Reflection
How would you modify your approach if you wanted to study whether:

1. There is a systematic difference in the model's bias for male vs. female NPs. 

2. There is a systematic difference in the model's biased for names vs. non-names. 

3. The model's IC verb bias aligned with human IC verb bias. 







