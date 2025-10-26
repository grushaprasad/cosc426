import torch
from torch.utils.data import DataLoader
import nltk
import pandas as pd

class LM_Dataset(torch.utils.data.Dataset):
    def __init__(self, data_fname, vocab_fname, max_length, lower=True):

        self.max_length = max_length
        self.vocab_fname = vocab_fname
        self.data_fname = data_fname
        self.lower = lower

        self.vocab = self.load_vocab()
        self.word_to_id, self.id_to_word = self.make_mapping()
        self.vocabSize = len(self.word_to_id)

        self.sentences, self.sentids = self.load_text()


        tokens_list = [['[BOS]'] + nltk.tokenize.word_tokenize(seq) + ['[EOS]'] for seq in self.sentences if len(seq)>0]


        self.tokenized = [[token.strip() for token in seq] for seq in tokens_list]


        self.encoded = [self.encode(seq) for seq in self.tokenized]

        self.X,self.y = self.make_pairs()

    def load_vocab(self):
        """
        Returns a set of all the words in the vocab file + [BOS] and [EOS]. Words in the vocab should be lowercased if self.lower is True. 

        """
        pass

    def load_text(self):
        """
        Returns sentences and sentids from the data file. 
        Sentences should be lowercased if self.lower is True.

        """
        pass



    def make_pairs(self):
        X = []
        y = []

        for seq in self.encoded:
            truncated = seq[:self.max_length]
            contexts = torch.tensor(truncated[:-1])
            targets = torch.tensor(truncated[1:])

            ## Left pad
            padded_contexts = torch.full((1,self.max_length), self.word_to_id['[PAD]'], dtype=torch.float).flatten()
            padded_contexts[-contexts.size(0):] = contexts

            padded_targets = torch.full((1,self.max_length), self.word_to_id['[PAD]']).flatten()
            padded_targets[-targets.size(0):] = targets


            X.append(padded_contexts)
            y.append(padded_targets)

        return X,y


    def make_mapping(self):

        special_tokens = {
            '[PAD]': 0,
            '[UNK]': len(self.vocab)+1
        }

        word_to_id = {}
        id_to_word = {}
        for i,word in enumerate(self.vocab):
            word_to_id[word] = i+1
            id_to_word[i+1] = word
        

        for key, val in special_tokens.items():
            word_to_id[key] = val
            id_to_word[val] = key

        return word_to_id, id_to_word

    def encode(self, seq):
        return [self.word_to_id[word] if word in self.vocab else self.word_to_id['[UNK]'] for word in seq]

    def decode(self, seq):
        return [self.id_to_word[ID] for ID in seq]

    def __getitem__(self, idx):

        x = self.X[idx]
        y = self.y[idx]

        return x,y

    def __len__(self):
        return len(self.X)


class LSTM_LM(torch.nn.Module):
    def __init__(self, vocabSize, nEmbed, nHidden, nLayers):
        super(LSTM_LM, self).__init__()
        self.vocabSize = vocabSize
        self.nHidden = nHidden
        self.nLayers = nLayers
        self.embed = torch.nn.Embedding(vocabSize, nEmbed)
        self.lstm = torch.nn.LSTM(nEmbed, nHidden, nLayers, batch_first=True)
        self.decoder = torch.nn.Linear(nHidden, vocabSize)  # ask them to explain this 

    def forward(self, X, hidden, cell):
        embedded = self.embed(X.long())
        output, (hidden, cell) = self.lstm(embedded, (hidden, cell))
        y_pred = self.decoder(output)
        return y_pred, hidden, cell

    def init_hidden(self, batchSize):
        hidden = cell =  torch.zeros((self.nLayers, batchSize, self.nHidden), dtype=torch.float)

        return hidden, cell

    def loss(self, y_pred, y_target):
        loss_fn = torch.nn.CrossEntropyLoss() ## takes logits not probs
        return loss_fn(y_pred, y_target)

class LM_Trainer():
    def __init__(self, num_epochs, lr, batch_size, device):
        self.num_epochs = num_epochs
        self.lr = lr
        self.batch_size = batch_size
        self.device = device

    def train(self, model, train_data, val_data):
        optimizer = torch.optim.SGD(model.parameters(), lr=self.lr, momentum=0.9)

        train_loader = DataLoader(train_data, batch_size = self.batch_size, shuffle=True) 

        evaluator = LM_Evaluator(val_data, self.device)

        for epoch in range(self.num_epochs):
            epoch_loss = 0
            num_batches = 0

            for batch in train_loader:
                X,y_target = batch
 
                num_batches+=1

                hidden, cell = model.init_hidden(X.size(0))

                X,y_target = X.to(self.device), y_target.to(self.device)
                y_pred, hidden, cell = model(X, hidden, cell)

                y_pred_reshaped = y_pred.reshape(-1, model.vocabSize) 

                loss = model.loss(y_pred_reshaped, y_target.flatten().long())


                optimizer.zero_grad()
                loss.backward()
                torch.nn.utils.clip_grad_norm_(model.parameters(), 0.25) 
                optimizer.step()
                epoch_loss += loss.item()


            if epoch%10 == 0:
                val_loss = round(evaluator.compute_loss(model), 5)

                print(f"Epoch {epoch}:\t Avg Train Loss: {round(epoch_loss/num_batches,5)}\t Avg Val Loss: {val_loss}")


class LM_Evaluator():
    def __init__(self, test_data, device):
        self.test_loader = DataLoader(test_data, batch_size = 1, shuffle=False)
        self.device=device
        self.cols = ['token', 'sentid', 'word', 'wordpos', 'model', 'tokenizer', 'punctuation', 'prob', 'surp']
        self.data = test_data

    def get_word_prob(self, words, all_probs):
        """
        Params:
            words: tensor of all word ids in a sequence

            all_probs: tensor of probabilities of all words in the vocab for each word in the sequence

        Returns: 
            tensor of probabilty of each word in the sequence 

        """

        word_probs = all_probs[torch.arange(len(words)), words]

        return word_probs

    @torch.no_grad()
    def compute_loss(self, model):
        """
        Returns the loss of the model on the test_data.

        """
        total_loss = 0
        for i, datapoint in enumerate(self.test_loader):
            X,y_target = datapoint
            hidden, cell = model.init_hidden(X.size(0))

            X,y_target = X.to(self.device), y_target.to(self.device)
            y_pred, hidden, cell = model(X, hidden, cell)

            y_pred_reshaped = y_pred.reshape(-1, model.vocabSize) 

            loss = model.loss(y_pred_reshaped, y_target.flatten().long())

            total_loss += loss.item()
        return total_loss/(i+1)


    @torch.no_grad()
    def get_preds(self, model):
        """
        Returns two nested lists with one sublist per sequence in the test data
        - words: each sublist has the word ids for each of the words in the sequence
        - probs: each sublist has the probability for each of the words in the sequence. 

        Hint 1: You should use the get_word_prob helper function to go from model output to probability.

        Hint 2: Pytorch has an inbuilt softmax function that can convert logits to probabilities.   

        """
        pass

    def save_preds(self, models, fpath):
        """
        Params:
            models: dictionary with model names as keys, model objects as values
            fpath: the path where the predictions should be saved

        Returns:
            Nothing. But saves a tsv file with columns in self.cols

        """
        pass






















