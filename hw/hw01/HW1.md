# COSC 426 F24 HW 1
### The HW is due on September 30 2024. You should work on your own for this HW

In the Lab 3 we worked with the Standard American English dialect. Some of the sentences that were ungrammatical in this dialect can be grammatical in other dialects. For example, the following sentences considered grammatical by (at least some) speakers of Indian English in specific situations.

- the panda gave/sent/lent the sandwich to my friend 
- the panda gave/sent/lent the sandwich
- the panda gave/sent/lent 
- the excited panda gave/sent/lent the sandwich in the pajamas to my ponderous friend very very joyfully
- the excited panda gave/sent/lent the sandwich in the pajamas very very joyfully
- the excited panda gave/sent/lent very very joyfully

The following sentences, however, are considered ungrammatical. 

- the panda gave/sent/lent to my friend 
- gave/sent/lent the sandwich 
- gave/sent/lent the sandwich to my friend


Note, these sentences do not make up the comprehensive set of grammatical and ungrammatical sentences, but are just illustrative examples. 

Your goal in this homework is to evaluate if the pretrained LM `distilgpt` treats sentences from Indian English as being grammatical

## Provided files

- [`HW1.py`](HW1.py)
- [Google doc template](https://docs.google.com/document/d/1vQolsfncqGbVwt4DWeV2HZhZDCbYm9N6x0M3-Dz1ZYA/edit?usp=sharing) to write your answers

## To submit

- `HW1.py` with the main function implemented which tests your grammar and creates training and validation data
- `hw1_grammar.txt` with the rules for Indian English implemented along with the rules from Lab3 implementing the adjectives and adverbs. 
- A pdf file of the google doc template with the answers filled out
- Any config or tsv files you created

**Make sure that your grammar from Lab3 works as intended before trying to modify it**

## Part 1: Adapting grammar to Indian English

Based on the examples above, what is the difference between Standard American English and Indian English dialects? Modify your grammar so it can accept sentences from Indian English. Write test cases to test your grammar. 

## Part 2: Setting up the appropriate minimal pair contrast

In this part your goal is to evaluate if the pretrained LM `distilgpt` treats sentences from Indian English as being grammatical. One approach to do this is to embed the sentence in a fronted sentential complement.  

For example, if you wanted to verify that a sentence like `the panda gave/sent/lent the sandwich`, you could compare the following minimal pairs. 

- `the fact that the panda gave/sent/lent the sandwich annoyed my friend`
- `the fact that the panda gave/sent/lent the sandwich to the pajamas annoyed my friend `

You could swap out annoyed with verbs like `perplexed` and `surprised`. 

In the google doc template, answer the following questions: 

1. Which word(s) in the minimal pair would you look at and why? (i.e., what is the `ROI`)
2. If `distilgpt` considered sentences from Indian English to be grammatical, what patterns would you expect to see in the `microdiff` column or the `accuracy` column of your results file? Why? 
3. Test your intuitions using the interact mode for one minimal pair. Include screenshots. What do you observe and what do you think it tells you? 

## Part 3: Does distilgpt treat sentences from Indian English as being grammatical? 

In this part you should use the NLP Scholar pipeline to more systematically evaluate whether `distilgpt` treats Indian English sentences as being grammatical.

Here are some things you should figure out before you run the pipeline: 

- How many types of minimal pairs do you want to have? 
- For your sentences, what would be your `sentid`, `pairid`, `contextid` and `condition`?
- What `lemma`s can you use? 

In the google doc template answer the following questions: 

1. What was your prediction? Why? 
2. What do you observe? Were any of the results surprising? Why or why not?   

## Part 4: Finetuning distilgpt on sentences from Indian English 

Generate 10000 sentences from your grammar with a maximum depth of 6. Finetune `distilgpt` model on this data. Use 90% of the sentences for your training, and 10% for validation. 

## Part 5: Does finetuning change how distilgpt treat sentences from IE?

Evaluate your finetuned model on the same sentences from Indian Englsh. 

In the google doc template answer the following questions: 

1. What was your prediction? Why? 
2. What do you observe? Were any of the results surprising? Why or why not?  

## Part 6: Discussion/ Reflection

What are the limitations of the experiment you ran? What are some changes you would make to the experimental setup if you wanted to more robustly study the following questions: 

1. Does distilgpt treat sentences from different dialects as being equally grammatical? 
2. Does finetuning distilgpt on specific dialects result in the model treating sentences from the dialects as being more grammatical? 





