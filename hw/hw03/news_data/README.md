# Introduction to MIND and MIND-small datasets

The following is adapted from the information provided in the msnews repo
[here](https://github.com/msnews/msnews.github.io/blob/master/assets/doc/introduction.md).
The dataset was introduced in [MIND: A Large-scale Dataset for News
Recommendation](https://aclanthology.org/2020.acl-main.331) (Wu et al., ACL
2020). The full datasets can be download, as mentioned in the paper,
[here](https://msnews.github.io/). The data in `MIND_small_train_news.tsv` is
from the small sample provided. Three major changes have been applied: 

1. Entries without an Abstract was dropped.
2. Entries with an Abstract larger than 480 tokens (with `bert-base-cased`) were
   dropped.
3. The entities columns were dropped. 

## Overall Introduction

The MIND dataset for news recommendation was collected from anonymized behavior
logs of <a href="https://microsoftnews.msn.com/">Microsoft News</a> website.  We
randomly sampled 1 million users who had at least 5 news clicks during 6 weeks
from October 12 to November 22, 2019.  To protect user privacy, each user is
de-linked from the production system when securely hashed into an anonymized ID.
We collected the news click behaviors of these users in this period, which are
formatted into impression logs.  We used the impression logs in the last week
for test, and the logs in the fifth week for training.  For samples in training
set, we used the click behaviors in the first four weeks to construct the news
click history for user modeling.  Among the training data, we used the samples
in the last day of the fifth week as validation set.  In addition, we release a
small version of MIND (**MIND-small**), by randomly sampling 50,000 users and
their behavior logs.  Only training and validation sets are contained in the
MIND-small dataset.


The datasets are intended for non-commercial research purposes only to promote
advancement in the field of artificial intelligence and related areas, and is
made available free of charge without extending any license or other
intellectual property rights. The dataset is provided “as is” without warranty
and usage of the data has risks since we may not own the underlying rights in
the documents. We are not be liable for any damages related to use of the
dataset. Feedback is voluntarily given and can be used as we see fit. Upon
violation of any of these terms, your rights to use the dataset will end
automatically. If you have questions about use of the dataset or any research
outputs, we encourage you to undertake your own independent legal review. For
other questions, please feel free to contact us at mind@microsoft.com.
 
### `MIND_small_train_news.tsv`

It has 5 columns, which are divided by the tab symbol:

* News ID 
* Category 
* SubCategory
* Title
* Abstract
* URL (We are sorry that many of the URLs have expired now)

The full content body of MSN news articles are not made available for download,
due to licensing structure. However, for your convenience, we have provided a
[utility script](https://github.com/msnews/MIND/tree/master/crawler) to help
parse news webpage from the MSN URLs in the dataset. Unfortunately, these URLs
have expired now and cannot be accessed. One possible way to get the news
content is using search engines with the news title.

An example is shown in the following table:

Column | Content
------------- | -------------
News ID | N37378
Category | sports
SubCategory | golf
Title | PGA Tour winners
Abstract | A gallery of recent winners on the PGA Tour.
URL | https://www.msn.com/en-us/sports/golf/pga-tour-winners/ss-AAjnQjj?ocid=chopendata
