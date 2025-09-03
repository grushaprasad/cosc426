# COSC 426 F25 Lab 1

## Introduction

The goal of this lab is to familiarize you to the `evaluate` and `analyze` mode of the NLPScholar toolkit. There are three parts: 
* Part 1: Minimal Pair
* Part 2: Token classification
* Part 3: Text classification 

Note the parts of the lab are ordered to be from (what I expect to be) the most to least challenging. The inention behind this is for you to spend time on the most challenging parts in lab, and work on the less challenging parts outside of lab if needed. So don't be disheartened if you find yourself spending a lot of time on the initial parts! 

## Submission instructions

Submit the following files to gradescope:

* `Lab1.ipynb` with answers to all of the questions. **Make sure that when you submit the file, the outputs in the cells are visible on gradescope.** 
* All config files you created. Create a separate file for each config setting you use. 

## Part 0: Setup

### Update NLPScholar

Before every lab and HW make sure to get the most recent version of NLPScholar by going into the directory and typing: 

`git pull`

### Recommended directory structure

COSC426
* NLPScholar 
* cosc426 
    * labs
        * lab00
        * lab01
            * starter_configs
            * data
            * predictions
            * results
            * Lab1.md
            * Lab1.ipynb
    * hw
        * HW1
        * HW2
* Midterm 
* Final project


## Part 1: MinimalPair

In this part you will be working with three models: 
* `gpt2`
* `distilbert/distilgpt2`
* `distilbert-base-uncased`

Answer the following questions for all the three models: 

1. What is the difference in surprisal between expected and unexpected when the verb lemma is `LIKE` when we consider the words specified in the ROI column?

2. Is the difference in surprisal between expected and unexpected greater for singular verbs compared to plural verbs when we consider the words specified in the ROI column? 

3. Is the answer to question 2 different if you look at the surprisal of the entire sentence? 

4. What is the mean probability of the expected (i.e., grammatical) sentences in `agreement.tsv` (over the entire sentence)?

5. What is the mean probability of the word `chameleons` in the expected sentences when you consider the period vs. not (i.e., `chameleons` vs. `chameleons.`)

After you are done with this, answer the following question: 

6. What is bad about `minimal_pairs_bad.tsv`? What happens when you run `evaluate` on this data file? What happens when you run `analyze` on this data file? 

## Part 2: TokenClassification

In this part you will be working on a [Named Entity Recogniton](https://en.wikipedia.org/wiki/Named-entity_recognition) task with the following model: 
* `distilbert-base-uncased`

Note: this model not been trained on the NER task. When you specify the model, you are just getting the architecture from Huggingface. So we should expect poor performance.  

Answer the following questions: 

1. What is the overall accuracy of the model?
2. What is the overall accuracy of the model if you ignore the `O` label (which indicates that there is no entity)
3. What is the overall accuracy if you ignore punctuation and the `O` label?
4. What is the accuracy of the `B-location` tag when you consider long vs. short sentences? 

After you are done with this, answer the following question: 

5. Here is a model that has been trained on NER task: [bert-base-NER](https://huggingface.co/dslim/bert-base-NER/tree/main). **This model has been trained on a different set of labels than the model you were evaluating.** If you wanted to use this model instead, what would you need to change in your NLPScholar config file? (*Hint: It might be helpful to look at the model's `config.json`*)


## Part 3: TextClassification

In this part you will be working on a Sentiment Analysis task with the following models: 
* `siebert/sentiment-roberta-large-english` (which has been trained on sentiment analysis)
* `roberta-large` which has not been trained (like in the TokenClassification example)

Answer the following questions:

1. Is the accuracy of trained model greater than the untrained model? 
2. Is the difference between the trained and untrained model greater for full vs. one-line reviews? 
3. Is the f1 score for reviews that are positive greater than f1 score for reviews that are negative when you consider all reviews and all models? 
4. Is the answer to 3 different if you consider just the ChatGPT generated reviews? 
5. What is the average probability of the predicted label for both the models? 





