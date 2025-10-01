{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3356241a-7e20-42d3-8f00-7f6707b65b5f",
   "metadata": {},
   "source": [
    "# Lab 5: Bayesian Classification\n",
    "### COSC 426: Fall 2025, Colgate University"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c4c04158-1b47-4004-ae8f-1c0e9196de01",
   "metadata": {},
   "source": [
    "## Part 1: Build a unigram model\n",
    "\n",
    "#### Part 1.1\n",
    "\n",
    "Start by understanding what is happening when you initilize a UnigramModel object"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa55c9ea-afde-4395-88a1-25a9ef8f0727",
   "metadata": {},
   "outputs": [],
   "source": [
    "from UnigramModel import UnigramModel\n",
    "import util\n",
    "import math\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "sample_model = UnigramModel(tokenize = util.nltk_tokenize,\n",
    "                            tokenizer_kwargs = {},\n",
    "                            vocab = util.get_vocab('data/glove_vocab.txt'),\n",
    "                            unk_token = '[UNK]',\n",
    "                            train_paths = ['data/sample-alice.txt'],\n",
    "                            smooth = 'add-0.1',\n",
    "                            lower = True\n",
    "                           )                    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "064d39c6-b2ec-4a61-93f2-34136ccee179",
   "metadata": {},
   "source": [
    "**What are the parameters required to initialize a `UnigramModel` object and how are these parameters used in the `UnigramModel` class?**\n",
    "\n",
    "\n",
    "[ANSWER HERE]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c9d7a210-9f67-4c49-9564-85f5fc5c1377",
   "metadata": {},
   "source": [
    "#### Part 1.2\n",
    "\n",
    "Verify your implementation of `get_prob` and `evaluate` with the code below. \n",
    "\n",
    "*Hint: Running into errors `get_probs`? Think carefully about when are where preprocessing is being applied in the pipeline, and what the expected input for `get_probs` is. Also think about how you want to handle word to not exist in training data and/or not in vocab*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b9c3e702-a3b5-4500-bc97-db4ecfaffb8e",
   "metadata": {},
   "outputs": [],
   "source": [
    "## print prob of words\n",
    "expected_probs = {'rabbit': 0.00010176146615934851,\n",
    "                  'it': 0.0002755005547240899,\n",
    "                  '[UNK]': 0.00017622107554423767,\n",
    "                  'Alice': 0.00017622107554423767,\n",
    "                  'Rabbit': 0.00017622107554423767,\n",
    "                  'maze': 2.4819869794963054e-06\n",
    "                 }\n",
    "\n",
    "for word in expected_probs:\n",
    "    if sample_model.get_prob(word) != expected_probs[word]:\n",
    "        print(word, '\\t incorrect')\n",
    "        print('expected', expected_probs[word])\n",
    "        print('got', sample_model.get_prob(word))\n",
    "        print()\n",
    "        \n",
    "\n",
    "## Create paths and then load it\n",
    "sample_model.evaluate(datafpath= 'data/sample-alice.txt',\n",
    "                      predfpath = 'predictions/my_sample_preds_alice.tsv')\n",
    "\n",
    "\n",
    "\n",
    "correct_df = pd.read_csv('predictions/my_sample_preds_alice.tsv', sep='\\t')\n",
    "my_df = pd.read_csv('predictions/sample_preds_alice.tsv', sep='\\t')\n",
    "\n",
    "\n",
    "# Does element wise comparison\n",
    "print('Are dfs same?', correct_df.equals(my_df))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f5100a57-2064-4b98-a324-a170c0f7a588",
   "metadata": {},
   "source": [
    "## Part 2: Implement building blocks of a Naive Bayesian Classifier\n",
    "\n",
    "Implement the building blocks for a Bayesian classifier. Here is a function that might be useful. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e79b6f41-3deb-439d-a3a4-fb2700893aab",
   "metadata": {},
   "source": [
    "### Part 2.1: Describe your approach\n",
    "\n",
    "**WRITE YOUR ANSWER HERE**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "51b94e34-9d46-4f7f-9355-80d8e547eec7",
   "metadata": {},
   "source": [
    "### Part 2.2 Implement functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c03a902-94c0-494e-958b-0cdd34350c5b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "def summarize(fname:str, aggregrate_type:str, aggregrate_col:str, groupby_cols:list, delimiter='\\t'):\n",
    "    \"\"\"\n",
    "    Args:\n",
    "        fname: fpath to tsv/ csv file\n",
    "        aggregate_type: mean or sum\n",
    "\n",
    "        aggrefate_col: the column with values you want to aggregate over\n",
    "\n",
    "        groupby_cols: the columns with the groups. \n",
    "\n",
    "    Returns:\n",
    "        Pandas Dataframe with as many rows as unique group combinations. The values of rows in each group is either summed together or averaged depending on the aggregate_type. \n",
    "\n",
    "    \"\"\"\n",
    "    dat = pd.read_csv(fname, sep=delimiter)\n",
    "\n",
    "    summ = dat.groupby(groupby_cols).agg({aggregrate_col: aggregrate_type}).reset_index()\n",
    "\n",
    "    return summ"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6689d474-0107-4f15-954a-3f726fc06d78",
   "metadata": {},
   "source": [
    "#### **Calculating the likelihood**\n",
    "\n",
    "Start by calculating the likelihood of some text given models trained on text from different classes --- i.e., $P(text \\mid model=class1)$, $P(text \\mid model=class2)$, etc\n",
    "\n",
    "*Hint: Think about why `summarize` function provided is useful* "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79577b49-c040-4df9-83c9-dc23c2a165b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_likelihood(models_dict, eval_fpath, class_label):\n",
    "    \"\"\"\n",
    "    Params:\n",
    "        models_dict: keys are classes and values are the models trained on the classes\n",
    "        eval_fpath: the file models should be evaluated on\n",
    "        class_label: the correct class label for sequences in the file \n",
    "\n",
    "    Returns:\n",
    "        A Dataframe with the following columns: \n",
    "            sentid: id of the sentence\n",
    "            model: the model being used to generate the likelihood\n",
    "            likelihood: the sum of log probability across all the words in the sequence\n",
    "            target_class: same as class_label\n",
    "        \n",
    "    \"\"\"\n",
    "    pass\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca9474e0-d9a6-42d7-a2b3-9386be26d280",
   "metadata": {},
   "source": [
    "Once you've implemented this function, verify that your output matches the expected output below. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d58a3705-d506-400b-a186-e10e9e382085",
   "metadata": {},
   "outputs": [],
   "source": [
    "sample_models = {\n",
    "    'alice': UnigramModel(tokenize = util.nltk_tokenize,\n",
    "                            tokenizer_kwargs = {},\n",
    "                            vocab = util.get_vocab('data/glove_vocab.txt'),\n",
    "                            unk_token = '[UNK]',\n",
    "                            train_paths = ['data/sample-alice.txt'],\n",
    "                            smooth = 'add-0.1',\n",
    "                            lower = True\n",
    "                           ),\n",
    "    'sherlock': UnigramModel(tokenize = util.nltk_tokenize,\n",
    "                            tokenizer_kwargs = {},\n",
    "                            vocab = util.get_vocab('data/glove_vocab.txt'),\n",
    "                            unk_token = '[UNK]',\n",
    "                            train_paths = ['data/sample-sherlock.txt'],\n",
    "                            smooth = 'add-0.1',\n",
    "                            lower = True\n",
    "                           )\n",
    "}\n",
    "\n",
    "my_df = get_likelihood(sample_models, 'data/sample-lookingglass.txt', 'alice').reset_index(drop=True)\n",
    "correct_df = pd.read_csv('predictions/sample-likelihood.tsv', sep='\\t').reset_index(drop=True)\n",
    "\n",
    "#using this instead of equal because of floating point imprecision\n",
    "print('Printing proportion of matched values across correct_df and my_df\\n')\n",
    "print('likelihood', np.isclose(my_df['likelihood'], correct_df['likelihood']).sum()/len(my_df)) \n",
    "for col in ['sentid', 'model', 'target_class']:\n",
    "    print(col, (my_df[col] == correct_df[col]).sum()/len(my_df))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "21711e91-0b7f-449e-a7d8-dde7227f8f84",
   "metadata": {},
   "source": [
    "#### Calculating the prior"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "09daf921-49e0-4e3f-8ff3-8d0b8307d889",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_prior(data: dict, tokenizer) -> dict:\n",
    "    \"\"\"\n",
    "    Args:\n",
    "        data: dictionary where keys are the classes, and values are filepaths to the class specific data\n",
    "\n",
    "    Returns:\n",
    "        Dictionary with prior probability for each class, which is the number of words in the class divided by the total number of words across all classes. \n",
    "        What counts as a word is determined by the tokenizer\n",
    "\n",
    "    \"\"\"\n",
    "    pass\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da052a32-3251-4fa5-8290-4e166b20fedf",
   "metadata": {},
   "outputs": [],
   "source": [
    "dat_dict = {'sherlock': ['data/sample-sherlock.txt'],\n",
    "            'alice': ['data/sample-alice.txt']}\n",
    "\n",
    "correct_prior = {'sherlock': 0.4423076923076923, 'alice': 0.5576923076923077}\n",
    "get_prior(dat_dict)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "af75a096-f34d-4eaf-bdd5-5168161d0253",
   "metadata": {},
   "source": [
    "#### Compute posterior\n",
    "\n",
    "*Hint: Think about why `summarize` function provided is useful*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ccfa1a27-5fde-416f-8b86-2c4eb18edefe",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_posterior(models_dict, eval_fpath, class_label, prior_dict):\n",
    "    \"\"\"\n",
    "    Args:\n",
    "        Dictionary where keys are classes and values are the models trained on the classes\n",
    "\n",
    "        eval_fpath: the file models should be evaluated on. \n",
    "\n",
    "        class_label: the label of the file that models are evaluated on\n",
    "\n",
    "        prior_dict: prior probabilities of classes\n",
    "\n",
    "    Returns:\n",
    "        A Dataframe with the following columns: sentid, model, likelihood, class. \n",
    "\n",
    "    If you set eval_fpath to sample_reviews_test_positive.txt, you should get a dataframe that looks like this. (Its ok if you end up having additional columns)\n",
    "\n",
    "   sentid model     likelihood   class        prior      posterior\n",
    "       0  positive  -100.975898  positive    -0.736966   -101.712864\n",
    "       1  positive  -100.941133  positive    -0.736966   -101.678099\n",
    "       0  negative  -101.938780  positive    -1.321928   -103.260708\n",
    "       1  negative  -101.938780  positive    -1.321928   -103.260708\n",
    "\n",
    "\n",
    "    \"\"\"\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3072a5c3-f810-401c-8fa1-2450a2983d95",
   "metadata": {},
   "outputs": [],
   "source": [
    "my_df = get_posterior(sample_models, \n",
    "                    'data/sample-lookingglass.txt',\n",
    "                    'alice',\n",
    "                     get_prior(dat_dict)).reset_index(drop=True)\n",
    "\n",
    "correct_df = pd.read_csv('predictions/sample-posterior.tsv', sep='\\t').reset_index(drop=True)\n",
    "print('posterior', np.isclose(my_df['posterior'], correct_df['posterior']).sum()/len(my_df)) \n",
    "          "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "042209e7-e0b5-48f0-938e-9fa8ad00573a",
   "metadata": {},
   "source": [
    "#### Implement classify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7c6cd5e-850f-4235-8c10-284d4040d589",
   "metadata": {},
   "outputs": [],
   "source": [
    "def classify(posterior):\n",
    "    \"\"\"\n",
    "    Args:\n",
    "        Dataframe with posterior probabilities\n",
    "\n",
    "    Returns: \n",
    "        Dataframe where each sentence id is associated with a prediction. \n",
    "    \"\"\"\n",
    "\n",
    "    # converts the data from long to wide\n",
    "    classes = posterior['model'].unique()\n",
    "    wide_df = posterior.pivot(index=['sentid', 'target_class'],\n",
    "                              columns=['model'],\n",
    "                              values='posterior').reset_index()    \n",
    "    #Finish the rest of the function \n",
    "\n",
    "    pass\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0fab057-a729-4dad-b951-079b2295cd29",
   "metadata": {},
   "outputs": [],
   "source": [
    "posterior = get_posterior(sample_models, \n",
    "            'data/sample-lookingglass.txt',\n",
    "            'alice',\n",
    "             get_prior(dat_dict)).reset_index(drop=True)\n",
    "my_df = classify(posterior).reset_index(drop=True)\n",
    "\n",
    "correct_df = pd.read_csv('predictions/sample-classify.tsv', sep='\\t').reset_index(drop=True)\n",
    "print('pred', (my_df['pred']==correct_df['pred']).sum()/len(my_df)) \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "835d7d31-6c44-4ec8-a51f-4ceb5adf8e96",
   "metadata": {},
   "source": [
    "#### Compute accuracy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9af4294d-9418-41da-8386-8b2e26d1be6e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def analyze(models_dict, eval_dict, prior_dict):\n",
    "    \"\"\"\n",
    "    Args:\n",
    "        models_dict: keys are classes, values are models trained on data from the class. \n",
    "\n",
    "        eval_dict: keys are classes, values are fpaths to evaluation data where the correct label is the class associated with the key\n",
    "\n",
    "        prior_dict: keys are classes, values are prior probabilties of the classes. \n",
    "\n",
    "    Returns:\n",
    "        Float which is the accuracy of the predictions across all classes\n",
    "\n",
    "    \"\"\"\n",
    "\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df7d2694-ba6e-4476-92f4-e68bb294f872",
   "metadata": {},
   "outputs": [],
   "source": [
    "sample_models = {\n",
    "    'alice': UnigramModel(tokenize = util.nltk_tokenize,\n",
    "                            tokenizer_kwargs = {},\n",
    "                            vocab = util.get_vocab('data/glove_vocab.txt'),\n",
    "                            unk_token = '[UNK]',\n",
    "                            train_paths = ['data/sample-alice.txt'],\n",
    "                            smooth = 'add-0.1',\n",
    "                            lower = True\n",
    "                           ),\n",
    "    'sherlock': UnigramModel(tokenize = util.nltk_tokenize,\n",
    "                            tokenizer_kwargs = {},\n",
    "                            vocab = util.get_vocab('data/glove_vocab.txt'),\n",
    "                            unk_token = '[UNK]',\n",
    "                            train_paths = ['data/sample-sherlock.txt'],\n",
    "                            smooth = 'add-0.1',\n",
    "                            lower = True\n",
    "                           )\n",
    "}\n",
    "\n",
    "## for simplicity making eval the same as train\n",
    "sample_eval = {\n",
    "    'alice': ['data/sample-lookingglass.txt'],\n",
    "    'sherlock': ['data/sample-sherlock.txt']\n",
    "}\n",
    "\n",
    "sample_prior = get_prior({'sherlock': ['data/sample-sherlock.txt'],\n",
    "                          'alice': ['data/sample-alice.txt']})\n",
    "\n",
    "\n",
    "target_acc = 92.857\n",
    "\n",
    "analyze(sample_models, sample_eval, sample_prior)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7ad8cc45-0f9e-45ab-8ff0-bfb2d7a10f92",
   "metadata": {},
   "source": [
    "## Part 3: Build Naive Bayesian Sentiment Classifier\n",
    "Add as many code and markdown chunks as is helpful"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "97e3a0e5-504c-438a-8228-af42cb09007b",
   "metadata": {},
   "source": [
    "## Part 4 (optional): Build Bigram Bayesian Sentiment Classifier\n",
    "Add as many code and markdown chunks as is helpful"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "cosc410",
   "language": "python",
   "name": "cosc410"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
