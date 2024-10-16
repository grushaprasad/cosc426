import math
import csv

class BigramModel:
    def __init__(self, tokenizer, vocab_fname: str, train_fpath: dict, mark_ends: bool):
        self.tokenizer = tokenizer
        self.mark_ends = mark_ends
        self.vocab = self.getVocab(vocab_fname)

        self.train_dat= self.loadData(tokenizer, train_fpath, mark_ends)

        self.bigram_freqs = self.getBigramFreqs()

        self.unigram_freqs = self.getUnigramFreqs()


    def getVocab(self, vocab_fname):
        """
        Args: 
            vocab_fname: filepath to vocab file. Each line has a new vocab item

        Returns: 
            A set of all the vocabulary items in the file plus three additional tokens: 
                - [UNK] : to represent words in the text not in the vocab
                - [BOS] : to represent the beginning of sentences. 
                - [EOS] : to represent the end of sentences. 
            If you run this function on the glove vocab, it should return set with 400003 items.
        """
        pass


    def loadData(self, tokenizer, textfname, mark_ends: bool) -> list:
        """
        tokenizer: a function to tokenize a sequence into words
        textfname: fpath with data.  
        mark_ends: indicates whether sequences should start with [BOS] and end with [EOS]

        Returns: 
        A list of lists where each sublist consists of tokens from each sentence. 
        Use existing nltk functions to first divide the text into sentences, and then into words. 

        If you run preprocess on the text in sample_train.txt with mark_ends=True you should get the following list: 
            [['[BOS]', 'one', 'thing', 'was', 'certain', ',', 'that', 'the', '_white_', 'kitten', 'had', 'had', 'nothing', 'to', 'do', 'with', 'it', ':', '—it', 'was', 'the', 'black', 'kitten', '’', 's', 'fault', 'entirely', '.', '[EOS]'], ['[BOS]', 'for', 'the', 'white', 'kitten', 'had', 'been', 'having', 'its', 'face', 'washed', 'by', 'the', 'old', 'cat', 'for', 'the', 'last', 'quarter', 'of', 'an', 'hour', '(', 'and', 'bearing', 'it', 'pretty', 'well', ',', 'considering', ')', ';', 'so', 'you', 'see', 'that', 'it', '_couldn', '’', 't_', 'have', 'had', 'any', 'hand', 'in', 'the', 'mischief', '.', '[EOS]']]

        
        Note: Assume that in your data, each sequence is on a new line
        """
        pass



    def getBigramFreqs(self):
        """
        Args: object

        Hint: think here about where you should get your data from. 

        Returns: 
            dictionary with all bigrams that occur in the text along with frequencies. 
            Each key should be a tuple of strings of the format (first_token, second_token). 

            If you run this function on sample_text from above with mark_ends as True, it should return: 
            73 bigrams
            The following 3 bigrams should have count 2: ('for', 'the'), (kitten, had) and (. , [EOS])
            All other bigrams should have count of 1. 
        """
        pass

    def getUnigramFreqs(self) -> dict:
        """
        Args: object

        Hint: think here about where you should get your data from. 

        Returns: 
            dictionary with all unigrams that occur in the text along with frequencies. 

        """
        pass

    def getBigramProb(self, bigram, smooth):
        """
        Args:
            bigram: the tuple of the bigram you want the prob of
            smooth: MLE (no smoothing), add-k where you add k to all bigram counts. Returns -1 if invalid smooth is entered.  

            Hint: any other parameters you need you should make this an attribute of the object that you initialize once so you minimize redundant computation. 

        Returns:
            float with prob. 
            Return -1.0 if invalid smoothing value is entered. 

            Here are the probabilities for some bigrams from sample_train.txt
            
            MLE: 
                ('one', 'thing') 1.0
                ('kitten', 'had') 0.6666666666666666
                ('cat', 'had') 0.0
                ('had', 'had') 0.25
                ('on', 'the') 0.0
                ('held', 'a') 0.0
                ('zzzzzzz', 'the') 0.0

            add-0.1:
                ('one', 'thing') 2.749910627904593e-05
                ('kitten', 'had') 5.2495669107298645e-05
                ('cat', 'had') 2.4999187526405393e-06
                ('had', 'had') 2.7497044067762715e-05
                ('on', 'the') 2.4999812501406237e-06
                ('held', 'a') 2.4999812501406237e-06
                ('zzzzzzz', 'the') 2.4997312788875196e-06

        """

        pass


    def evaluate(self, eval_fpath, result_fpath, smooth):
        """
        Args: 
            eval_fpath: the path to the evaluation data
            result_fpath: path where predictions will be saved
            smooth: smoothing to be applied

        Output: 
            Creates a file with five columns: 
                sentid: id of the sequence 
                word: second word of the bigram (e.g., if bigram is 'kitten had', word would be had)
                wordpos: position of the word in the sentence
                prob: P(word | prev word)
                surp: - log_2 P(word | prev word)

            See sample_preds.tsv as an example. 

        """

        pass

        








