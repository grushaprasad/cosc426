import nltk
from transformers import AutoTokenizer
import os
import pickle
import csv


def get_ngrams(text: list, n):
    """
    Params:
        text: tokenized text in a list
        n: the n of the ngram

    Returns:
        list of all ngrams
    """
    return list(nltk.ngrams(text, n))


def get_ngramFreqs(text: list, n: int):
    """
    Params:
        text: text, split into list of tokens
        n: the n for ngram

    Returns:
        Frequnency dictionary
    """

    ngrams = get_ngrams(text, n)
    freq_dict = nltk.probability.FreqDist(ngrams)

    return freq_dict


def preprocess(textfname: str, lower: bool, tokenizer, **kwargs):
    """
    Params:
        textfname: path to text file.
        tokenizer: tokenizing function
        **kwargs: other kwargs for the tokenizer

    Returns:
        List of tokens in the text

    """
    tokens = []
    print(f"Reading {textfname}")
    with open(textfname, "r") as f:
        text = f.readlines()

    for i, line in enumerate(text):
        if lower:
            line = line.lower()
        tokens.extend(tokenizer(line, kwargs))
        if i % 100 == 0:
            print(f"Tokenized {i+1} lines")

    return tokens


def hf_tokenize(text: str, kwargs):
    """
    Params:
        text: string of text
        kwargs: dictionary with kwargs. Should include key 'modelname' which specifies the hf modelname
    Returns:


    """
    modelname = kwargs["modelname"]

    tokenizer = AutoTokenizer.from_pretrained(modelname)
    tokenized_output = tokenizer(text)
    words = tokenizer.convert_ids_to_tokens(tokenized_output["input_ids"])
    return words


def get_hf_vocab(modelname):
    """
    Params:
        modelname: string of hf modelname
    Returns:
        The vocabulary used by the huggingface model

    """
    tokenizer = AutoTokenizer.from_pretrained(modelname)
    return tokenizer.vocab


def tests():
    text = preprocess("data/test.txt", True, hf_tokenize, modelname="distilgpt2")
    print(text)
    bigram_freqs = get_ngramFreqs(text, 2)
    bigrams = get_ngrams(text, 2)

    for bigram in bigrams:
        if bigram_freqs[bigram] != 1:
            print(bigram, bigram_freqs[bigram])

    print(len(get_hf_vocab("distilgpt2")))


def train_ngram(text: list, n: int, vocab: set, smooth: str = "MLE"):
    """Get the probabilities of ngrams

    Returns:
        probs: dictionary of ngram probabilities
    """
    k = 0.0
    v = len(vocab)
    text.append("[UNK]")
    total_words = len(text)  # for unigram
    freqs = {}
    target_freqs = {}
    probs = {}

    if smooth.startswith("add-"):
        k = float(smooth[4:])
        if k < 0:
            raise ValueError("k must be non-negative")

    for i in range(1, n + 1):  # get all ngram freqs up to n
        ngram_freqs = get_ngramFreqs(text, i)
        freqs = freqs | ngram_freqs
        if i == n:
            target_freqs = ngram_freqs

    if n == 1:  # unigram
        for unigram, freq in target_freqs.items():
            probs[unigram] = (freq + k) / (total_words + k * v)
        return probs

    for ngram, freq in target_freqs.items():  # ngram
        pfreq = freqs[ngram[: n - 1]]  # context frequency
        probs[ngram] = (freq + k) / (pfreq + k * v)
    return probs


def evaluate(model: dict, eval_text: list, n: int):
    """Evaluate the n-gram model on a given text file.

    Returns:
        float: the average probability of the n-grams in the evaluation text.
    """
    total_prob = 0.0
    count = 0

    for i in range(len(eval_text) - n + 1):
        ngram = tuple(eval_text[i : i + n])
        total_prob += model.get(ngram, 0)
        count += 1

    if count == 0:
        return 0.0

    return total_prob / count


def preprocess_and_cache(
    textfname: str, lower: bool, tokenizer, cache_dir: str = "data/", **kwargs
):
    """
    Params:
        textfname: path to the text file
        lower: whether to convert text to lowercase
        tokenizer: tokenizing function
        cache_dir: path to save/load the cache file
        **kwargs: other kwargs for the tokenizer

    Returns:
        List of tokens in the text
    """
    cache_filename = f"{os.path.splitext(os.path.basename(textfname))[0]}_tokens.pkl"
    cache_filepath = os.path.join(cache_dir, cache_filename)

    try:
        with open(cache_filepath, "rb") as f:
            tokens = pickle.load(f)
        print(f"Loading preprocessed tokens from cache: {cache_filepath}")
    except (FileNotFoundError, EOFError):
        print(f"Cache not found or invalid at {cache_filepath}. Running preprocess...")
        tokens = preprocess(textfname, lower, tokenizer, **kwargs)

        print(f"Saving preprocessed tokens to cache: {cache_filepath}")
        with open(cache_filepath, "wb") as f:
            pickle.dump(tokens, f)

    print(f"Successfully processed {textfname}. Token count: {len(tokens)}\n")
    return tokens


def write_to_tsv(filepath, columns, rows):
    with open(filepath, "w") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(columns)
        for row in rows:
            if isinstance(row, str):
                writer.writerow([row])
            elif isinstance(row, list):
                writer.writerow(row)


if __name__ == "__main__":
    tests()
