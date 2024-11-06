# COSC 426 F24 Lab 8

## Introduction

In this homework you will build on Lab 8 to build a small news search engine.
In this lab you will build and evaluate a model for token classification.  By
completing this homework, you will demonstrate that you are able to use a token
classification model for a real world application. 

## Provided files

- `HW3.py`
- `news_data`

## What to submit

- `HW3.py` 
- evaluate config file

## Part 0: Setting Up

Pull the most recent version of `NLPScholar` using `git pull`. 

## Part 1: Our Goal (across the lab and the homework)

Our broad goal across the homework and the lab is to build a prototype news
search engine. As a motivating example, consider the following text: 

while eating an apple, the founder of apple thought of a logo in san francisco

We'd like to be able to label this text with labels, like that the second apple
and not the first apple is an organization and that san francisco is a location.
That way, people can search for apple and return only those articles about the
corporation and not the food, for example. 

In the lab, you built a model which tags data with labels. In the homework, you
will use this model on news data (contained in `news_data`) to build a news
search engine. 

`HW3.py` includes functions with docstrings that will help scaffold your
approach. **Please review these and follow up with your instructor prior to
continuing on if you don't understand what is provided.**

## Part 2: Building a search engine 

By the end of the homework, you should have a sample interface like: 


```
Entity tag (PER|LOC|ORG|STOP): DATE
Tag not in database
Entity tag (PER|LOC|ORG|STOP): LOC
Search phrase: Syracuse
         Four years ago, a jury convicted Robert Neulander, a prominent
         doctor in central New York, of killing his wife in their
         suburban home, seemingly ending a complicated case that had
         riveted the Syracuse area. It was actually about to get more
         complicated. On the day of the verdict, an alternate juror
         contacted a lawyer for Mr. Neulander.

         While this system didn't break any snow records in Syracuse, it brought
         plenty of cold. Record low maximum for Nov. 12 was shattered by five
         degrees, the new record of 27 was set on Tuesday and a new record low
         was also set in Syracuse for this date as the mercury dipped to the
         lower teens.

         Four years ago, a jury convicted Robert Neulander, a prominent
         doctor in central New York, of killing his wife in their
         suburban home, seemingly ending a complicated case that had
         riveted the Syracuse area. It was actually about to get more
         complicated. On the day of the verdict, an alternate juror
         contacted a lawyer for Mr. Neulander.

         Spencer Martin re-assigned to Syracuse and two forwards sent to
         Orlando.

Entity tag (PER|LOC|ORG|STOP): ORG
Search phrase: Colgate University
Phrase not found
```

Think through the steps of this. You will need to label the news data for tags.
You need to extract entities. And then, you need to build a database to allow
for searching. Use your `Lab8.py`. In case your model doesn't work well, I've
provided a trained ner model following the Lab 8 instructions. You should be
able to access it on turning at the following location (you should be able to
reference it in your config files): 

```
/datalake/fdavis/COSC426/ner_model
```

