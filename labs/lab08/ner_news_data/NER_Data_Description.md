# NER News Data

For the lab, we will train an encoder model for named entity recognition. For
that we need data. I have adapted
[data](https://huggingface.co/datasets/imvladikon/english_news_weak_ner) from
HuggingFace. 

The following files are provided: 

- `english_news_weak_ner_small_train.jsonl`
- `english_news_weak_ner_small_valid.jsonl`
- `english_news_weak_ner_small_test.jsonl`
- `sample_ner_evaluate_mode_data.tsv`

## Overall Introduction

The data for training a token classification model is provided in the jsonl
files. The format is data with the following columns: 

* `doc_id`
* `sent_num`
* `sentence`
* `doc_title`
* `score`
* `entity_type`
* `entity_text`
* `start_char`
* `end_char`
* `tokens`
* `raw_tags`
* `ner_tags`

We are primarily interested in `tokens` which contains the words in a list and
`ner_tags` which contains the tags. The mapping from id (in the `ner_tags`) to
labels (like `LOC`) is detailed on the HuggingFace repo
[link](https://huggingface.co/datasets/imvladikon/english_news_weak_ner). 


