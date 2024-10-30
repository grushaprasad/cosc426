# COSC 426 F24 Lab 7

## Introduction

Every team has to submit a final project proposal by **Tuesday November 5**. Part of the proposal requires you to operationalize your question in terms of the NLPScholar toolkit and come up with a minimal working example. In this lab you will spend time working on this part of the proposal. While you can definitely talk to others in the lab during this process (whether or not they are in your group), **you are expected to turn in all of the required components of the lab on your own**. This is because every member of the team is expected to be familiar with all of the project components. 

## Provided files

[A google doc template for the final project proposal](https://docs.google.com/document/d/1WhDwPMXrs0_b4svbO9RI5E4jZLQHGsJNZPMMfXL79fk/edit?usp=sharing)

## What to submit

- A pdf for Part 1
- Sample tsv files from Part 2
- Config files from Part 3
- Turing job submission files from Part 4
- README file from Part 5

## Part 0

Read through the template for the final project proposal to make sure you understand what is expected of you. **Ask for clarifications if things are unclear!**

## Part 1

Take your project topic and operationalize it in a way such that you can approach it using `NLPScholar`. Note: `NLPScholar` is currently not set up for specific tasks like text generation. If your project involves these tasks, reframe the topic in terms of something `NLPScholar` can handle (i.e., MinimalPair, TextClassification or TokenClassification). 

*Note: You can eventually choose to not use `NLPScholar` for the final project, but this is going to involve a lot more work on your end. So for this lab, we want to make sure that you can tackle at least some part of your project with `NLPScholar`.*

In a pdf file include the following details: 

- Your project topic
- The **sequence of steps** you will need to take to go from a dataset to a results table/ figure?
- A description of how these steps map on to different models in `NLPScholar`. 

## Part 2

For each step that uses `NLPScholar`, generate a sample tsv file that is formatted exactly as is required for the correspnding `NLPScholar` mode. This tsv file should be minimal (very few rows), but should have enough detail to capture all of the variability in your dataset (e.g., if you have three conditions,  you should have all three conditions in your tsv file). 


## Part 3

For each step that uses `NLPScholar`, write config files. You can set up the config file with `distilbert` or `distilgpt` for now, and change it later to whatever model you want to use for the final project. 

## Part 4

For each step that uses `NLPScholar`, write pbs scripts that you can use to submit this as a job to Turing. 

## Part 5

Write a README file that outlines in detail how you will go from the output of NLPScholar to your evaluation metrics / table/ figures. 






