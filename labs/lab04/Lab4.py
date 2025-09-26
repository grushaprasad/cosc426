import math
import doctest
import nltk
nltk.download('punkt_tab')

def getVocab(vocab_fname: str) -> set: 
    """
    Args: 
        vocab_fname: filepath to vocab file. Each line has a new vocab item

    Returns: 
        A set of all the vocabulary items in the file plus three additional tokens: 
            - [UNK] : to represent words in the text not in the vocab
            - [BOS] : to represent the beginning of sentences. 
            - [EOS] : to represent the end of sentences. 
        If you run this function on the glove vocab, it should return set with 400003 items.

    >>> len(getVocab('data/glove_vocab.txt'))
    400003
    """
    a = ['[UNK]','[BOS]','[EOS]']
    with open(vocab_fname) as f:
        for line in f:
            a.extend(line.lower().rstrip('\n').split())
    return a

def preprocess(textfname:str, mark_ends: bool) -> list:
    """
    Args: 
        text: some text

        mark_ends: indicates whether sentences should start with [BOS] and end with [EOS]

    Returns: 
        A list of lists where each sublist consists of tokens from each sentence. 
        Use existing nltk functions to first divide the text into sentences, and then into words. 

    >>> preprocess('data/test.txt', mark_ends=True)
    [['[BOS]', 'one', 'thing', 'was', 'certain', ',', 'that', 'the', '_white_', 'kitten', 'had', 'had', 'nothing', 'to', 'do', 'with', 'it', ':', '—it', 'was', 'the', 'black', 'kitten', '’', 's', 'fault', 'entirely', '.', '[EOS]'], ['[BOS]', 'for', 'the', 'white', 'kitten', 'had', 'been', 'having', 'its', 'face', 'washed', 'by', 'the', 'old', 'cat', 'for', 'the', 'last', 'quarter', 'of', 'an', 'hour', '(', 'and', 'bearing', 'it', 'pretty', 'well', ',', 'considering', ')', ';', 'so', 'you', 'see', 'that', 'it', '_couldn', '’', 't_', 'have', 'had', 'any', 'hand', 'in', 'the', 'mischief', '.', '[EOS]']]

    >>> preprocess('data/test.txt', mark_ends=False)
    [['one', 'thing', 'was', 'certain', ',', 'that', 'the', '_white_', 'kitten', 'had', 'had', 'nothing', 'to', 'do', 'with', 'it', ':', '—it', 'was', 'the', 'black', 'kitten', '’', 's', 'fault', 'entirely', '.'], ['for', 'the', 'white', 'kitten', 'had', 'been', 'having', 'its', 'face', 'washed', 'by', 'the', 'old', 'cat', 'for', 'the', 'last', 'quarter', 'of', 'an', 'hour', '(', 'and', 'bearing', 'it', 'pretty', 'well', ',', 'considering', ')', ';', 'so', 'you', 'see', 'that', 'it', '_couldn', '’', 't_', 'have', 'had', 'any', 'hand', 'in', 'the', 'mischief', '.']]

    """
    text = ""
    result = []
    with open(textfname) as f:
        for line in f:
            text += line
    
    sents = nltk.sent_tokenize(text)
    for sent in sents: 
        a =[]
        sent = sent.lower()
        if(mark_ends):
            a = ['[BOS]', *nltk.word_tokenize(sent), '[EOS]']
        else:
            a = nltk.word_tokenize(sent)

        result.append(a)
    return result
    

def TestBigramFreqs(freq_dict, print_non1 = False):
    """
    Helper function to use in doctest of getBigramFreqs

    """
    inverse = {}
    # inverse2 = {}
    for key,val in freq_dict.items():
        # inverse[val] = inverse.get(val, 0) + 1
        inverse[val] = inverse.get(val, []) 
        inverse[val].append(key)

    if print_non1:
        return {key: val for key, val in inverse.items() if key !=1}
    else:
        return {key: len(val) for key, val in inverse.items()}

def getBigramFreqs(preprocessed_text:list, vocab:set) -> dict:
    """
    Args: 
        preprocessed_text: text that has been divided into sentences and tokens


    Returns: 
        dictionary with all bigrams that occur in the text along with frequencies. 
        Each key should be a tuple of strings of the format (first_token, second_token). 

    >>> TestBigramFreqs(getBigramFreqs(preprocess('data/test.txt', mark_ends=True), getVocab('data/glove_vocab.txt')))
    {1: 70, 2: 3}

    >>> TestBigramFreqs(getBigramFreqs(preprocess('data/test.txt', mark_ends=True), getVocab('data/glove_vocab.txt')), print_non1=True)
    {2: [('kitten', 'had'), ('.', '[EOS]'), ('for', 'the')]}

    """
    frq = {}
    for sent in preprocessed_text: 
        words = [ word if word in vocab else '[UNK]' for word in sent ]
        for i in range(len(words)-1):    
            if ((words[i], words[i+1]) not in frq):
                frq[(words[i], words[i+1])] = 1
            else:
                frq[(words[i], words[i+1])] += 1
    return frq

def getBigramProb(bigram: tuple, smooth: str, **kwargs):
    """
    Args:
        bigram: the tuple of the bigram you want the prob of
        smooth: MLE (no smoothing), add-k where you add k to all bigram counts. Returns -1 if invalid smooth is entered. 
        **kwargs: other parameters you might want. 

        Hint: think about what parameters do you want to pass in so you minimize redundant computation. 

    Returns:
        float with prob. 
        Return -1.0 if invalid smoothing value is entered. 

        Here are the probabilities for some bigrams from data/test.txt
        
        MLE: 
            ('one', 'thing') 1.0
            ('kitten', 'had') 0.6666666666666666
            ('cat', 'had') 0.0
            ('had', 'had') 0.25
            ('on', 'the') 0.0
            ('held', 'a') 0.0
            ('zzzzzzz', 'the') 0.0

        add-1:
            ('one', 'thing') 4.999950000499995e-06
            ('kitten', 'had') 7.499887501687475e-06
            ('cat', 'had') 2.4999750002499977e-06
            ('had', 'had') 4.999912501531223e-06
            ('on', 'the') 2.499981250140624e-06
            ('held', 'a') 2.499981250140624e-06
            ('zzzzzzz', 'the') 2.4999562507656116e-06

    """
    k = 0 
    b = [bigram[0], bigram[1]]
    if smooth !='MLE' and not smooth.startswith('add-'):
        print("You are in     if smooth is not 'MLE' or not smooth.startswith('add-'):")
        return -1
    if smooth.startswith('add-'):
        try:
            k = float(smooth.lstrip('add-'))
        except:
            return -1

    # (frqbigram + k) / (w_1frq + VK)
    unigramfrq = kwargs['unigramfrq']
    bigramfrq = kwargs['bigramfrq']
    vocab:dict = kwargs['vocab']
    
    if bigram[0] not in vocab:
        b[0] = '[UNK]'
    if bigram[1] not in vocab:
        b[1] = '[UNK]'
    
    nu = k
    if tuple(b) in bigramfrq:
        nu = bigramfrq[tuple(b)] + k
    
    de = len(vocab)*k
    if b[0] in unigramfrq:
        de = unigramfrq[b[0]] + len(vocab)*k
    
    if not de:
        return 0.0
    return nu/de
    
def getUnigramFreqs(preprocessed_text:list, vocab:set) -> dict:
    frq = {}
    for sent in preprocessed_text: 
        words = [ word if word in vocab else '[UNK]' for word in sent ]
        for i in range(len(words)):    
            if (words[i] not in frq):
                frq[words[i]] = 1
            else:
                frq[words[i]] += 1
    return frq

def getTrainVocab(fn:str):
    a = ['[UNK]','[BOS]','[EOS]']
    with open(fn) as f:
        for line in f:
            a.extend(nltk.word_tokenize(line))
    a = list(set(a))
    a.sort()
    return a

def evaluate(fn:str, smooth:str, bigramfrq: dict, unigramfrq:dict, vocab:list):
    # smooth='add-1'
    text = preprocess(fn, True)
    total = 0
    count = 0
    for sent in text: 
        for i in range(len(sent)-1):
            total += getBigramProb((sent[i],sent[i+1]), smooth, bigramfrq=bigramfrq, unigramfrq=unigramfrq, vocab=vocab)
            count += 1
    
    return total/count 

def run_all_tests(target_file):
    smoothing_params = [2, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
    mark_ends_options = [True, False]

    print("="*70)
    print(f"Starting Evaluation on: {target_file}")
    print("="*70)

    vocab = getTrainVocab(target_file)

    for k in smoothing_params:
        smoothing_str = f'add-{k}'
        
        for mark_ends in mark_ends_options:
            text = preprocess(target_file, mark_ends)

            bigram_freqs = getBigramFreqs(text, vocab)
            unigram_freqs = getUnigramFreqs(text, vocab)

            score = evaluate(target_file, smoothing_str, bigram_freqs, unigram_freqs, vocab)

            mark_ends_label = str(mark_ends).lower()
            print(f'[{smoothing_str:>11}][mark the ends:{mark_ends_label:>5}] -> Score: {score:.4f}')
        
        if k != smoothing_params[-1]:
            print("-" * 70)

    print("="*70)
    print("Evaluation Complete.")
    print("="*70)