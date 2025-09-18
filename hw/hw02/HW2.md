# COSC 426 F25 HW2

## Introduction

In this homework, you will write a grammar for a simplified version of the language that Yoda from Star Wars speaks (which we'll call `yoda-speak`), and then evaluate the extent to which models capture aspects of `yoda-speak`. Concretely, this HW has three required parts, and one optional part: 

* Part 1: Write a grammar for `yoda-speak` 
* Part 2: Evaluate whether `distilgpt` treats sentences from `yoda-speak` as being grammatical
* Part 3: Finetune `distilgpt` on sentences from `yoda-speak`, and evaluate whether the finetuned model treats sentences from `yoda-speak` as being more grammatical than in Part 2. 
* Part 4 (optional): Train a `distilgpt` model from scratch on sentences from `yoda-speak`, and evaluate whether the finetuned model treats sentences from `yoda-speak` as being more grammatical than in Part 2 or 3. 

## Provided files
* `hw2_grammar_sae.txt` that generates the SAE versions of the sentences in the following section
* `HW2.py` which has some helpful functions (most of them from Lab 3)
* `HW2.ipynb`, which is where you will include your answers to the questions in all the parts. 

## Submission instructions

You should submit the following files to gradescope:
* `HW2.ipynb` with answers to questions from all the parts. 
* `hw2_grammar_yoda.txt` from Part 1
* `hw2_eval.tsv` from Part 2
* Any config files that you create for Parts 2, 3, (and 4 if you attempt it)
* Any other python files that you use (e.g., to create a systematic evaluation dataset)


## Describing `yoda-speak`

You can assume that `yoda-speak` uses the same words as Standard American English (SAE), but differs from SAE in the ways in which these words are combined. In this homework we will focus on three ways: 

### Word order

SAE uses a Subject-Verb-Object word order, where as `yoda-speak` uses `Object-Subject-Verb` word order for some verbs and a `Verb-Subject-Aux` for others. 

Here are some grammatical sentences in `yoda-speak` and the corresponding SAE sentences in parentheses. Note: the SAE sentences are ungrammatical in `yoda-speak`

1. the Force you seek (you seek the Force)
2. the path the Jedi follow (the Jedi follow the path)
3. you I teach (I teach you)
4. fight the Jedi do (the Jedi fight)
5. sleep you do (you sleep)



### Prepositional phrases attaching to VPs

In SAE, prepositional phrases (PPs) attach to the right of VPs and NPs. In `yoda-speak` PPs attach to the left of VPs, but the attachment for NPs is unchanged: it still attaches to the right of NPs. 

Here are some grammatical sentences in `yoda-speak` and the corresponding SAE sentences in parentheses. Note: as before, the SAE sentences are ungrammatical in `yoda-speak`. 

1. in the night fight the Jedi do (the Jedi fight in the night)

2. the Force through the darkness the Jedi seek (the Jedi seek the Force through the darkness)

3. the Jedi the darkness in the night teach (the darkness in the night teach the Jedi)

4. in the night in the rain fight the Jedi do (the Jedi fight in the night in the rain)

5. in the rain in the night fight the Jedi do (the Jedi fight in the night in the rain)


Note, the last two examples have the same SAE sequence, but different `yoda-speak` sequences. 

* 4 corresponds to the interpretation in SAE where "in the rain" attaches to NP "the night" (i.e., the rain was happening in the night)

* 5 corresponds to the interpretation in SAE where "in the rain" attaches to the VP "fight in the night" (i.e, the fighting is happening in the night and in the rain)



## Part 1: Writing a grammar for `yoda-speak`

For this part, do the following: 
* In `hw2_grammar_yoda.txt'`, write a grammar for `yoda-speak`. In this grammar, keep all of the terminals the same as in `hw2_grammar_sae.txt` and modify the non-terminals. 

* In `HW2.ipynb` verify that the grammar considers all of the above `yoda-speak` sentences as grammatical, and the SAE sentences as ungrammatical. 

IMPORTANT: You should make sure that:

*  NPs that are marked as SubjNP in the SAE parse are also marked as SubjNP in the `yoda-speak` parse. 
* NPs that are marked as ObjNP in the SAE parse are also marked as ObjNP in the `yoda-speak` parse. 
* If a PP is the sister of the verb in SAE, it is also the sister of the verb in `yoda-speak`

## Part 2: Evaluate whether `distilgpt` treats sentences from `yoda-speak` as being grammatical

In this part, you will compare the probability that the model assigns to `yoda-speak` sentences relative to English grammatical sentences and English ungrammatical sentences. Based on these results, interpret whether `distilgpt` treats `yoda-speak` as being grammatical. 

For this part, do the following: 

* Create `hw2_eval.tsv` which sets up the minimal pairs necessary for the experiment.  

* Run the minimal pair experiment.

* Report and discuss the results of the experiment in `HW2.ipynb`

In the TSV file, you should include the 10 sentences above. You can optionally also include a more comprehensive and systematic evaluation dataset for an exceeds expectations designation (see more under the "Grading section" at the end of the document). 

## Part 3: Finetune `distilgpt` on `yoda-speak` and evaluate it. 

In this part, you will use NLPScholar's `train` mode to finetune an existing model. You can find details about how to train a model under "Config details for train" in the NLPScholar README, also linked [here](https://github.com/forrestdavis/NLPScholar/tree/main?tab=readme-ov-file#config-details-for-train) for convenience. 

For this part, do the following: 

* Using the helper functions in `HW3.py`, create a dataset with 10000 sentences in `yoda-speak`. Take 90% of this for the required training file, and 10% of this for the required validation file.  

* Finetune a model on this dataset. (*Hint: to understand the difference between train and finetune look at the `loadPretrained` parameter*)

* Run the minimal pair experiment from Part 2 on this finetuned model. 

* Report and discuss the results of the finetuned model in `HW2.ipynb`. 



## Part 4 (Optional): Train  `distilgpt` on `yoda-speak` from scratch and evaluate it. 

For this part, you should: 

* Train `distilgpt` from scratch on sentences from `yoda-speak`
* Run the minimal pair experiment again
* Report and discuss the results in `HW2.ipynb`. 
* Discuss the difference between training and finetuning, why that might (or might not have) resulted in a difference in the results. 

## Grading

### Meets expectation designation

In order to get this designation, you should meet all of the following requirements: 

* Your `HW2.ipynb` demonstrates that your grammar correctly tackles all of the grammatical `yoda-speak` and ungrammatical `SAE` examples specified in this HW.  

* Your TSV file in Part 2 includes all of the grammatical sentences specified in this HW, and the minimal pairs are correctly set up. 

* You correctly create the dataset, finetune the model, and report the results of the finetuned model. 

* You submit all of the required files.

### Exceeds expectation designation

In order to get this designation, you should meet at least one of the following requirements: 

* You create a more systematic evaluation dataset for Part 2, and motivate your choice. 

* You correctly complete Part 4, and include a thoughtful comparison between finetuning and training. 



