import torch
from torch.utils.data import DataLoader
import nltk

class CBOW_Dataset(torch.utils.data.Dataset):
    def __init__(self, fname, vocab_fname, window_size):
        with open(fname, 'r') as f:
            self.text = f.read().lower()

        with open(vocab_fname, 'r') as f:
            words = [word.strip() for word in f.readlines()] + ['[BOS]', '[EOS]']
            self.vocab = set(words)

        tokens_list = [['[BOS]'] + nltk.tokenize.word_tokenize(seq) + ['[EOS]'] for seq in self.text.split('\n')]


        self.tokenized = [[token.strip() for token in seq] for seq in tokens_list]

        self.word_to_id, self.id_to_word = self.make_mapping()

        self.encoded = [self.encode(seq) for seq in self.tokenized]

        self.window_size = window_size

        self.vocabSize = len(self.word_to_id)

        self.X,self.y = self.make_pairs()

       

    def make_pairs(self):
        X = []
        y = []
        for seq in self.encoded:
            for i in range(len(seq)):
                start = max(0,i - self.window_size)
                end = min(len(seq), i+self.window_size + 1)

                left_pad = [self.word_to_id['[PAD]']]*(self.window_size-i)

                right_pad = [self.word_to_id['[PAD]']]*((i+self.window_size + 1)-len(seq))



                left = left_pad + seq[start : i]
                right = seq[i + 1 : end] + right_pad

                context = left + right

                target = seq[i]


                X.append(torch.tensor(context))
                y.append(torch.tensor(target))

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
        # return [self.word_to_id[word] for word in seq]

    def decode(self, seq):
        return [self.id_to_word[ID] for ID in seq]

    def __getitem__(self, idx):

        x = self.X[idx]
        y = self.y[idx]

        return x,y

    def __len__(self):
        return len(self.X)


class CBOW_Model(torch.nn.Module):
    def __init__(self, nEmbed, vocabSize):
        super(CBOW_Model, self).__init__()

        self.embed = torch.nn.Embedding(vocabSize, nEmbed)

        self.out = torch.nn.Linear(nEmbed, vocabSize)



    def forward(self, inp):
        embedded_inp = self.embed(inp)
        avg_inp = embedded_inp.mean(dim=1)
        logits = self.out(avg_inp)

        return logits

    def loss(self, y_pred, y_target):
        loss_fn = torch.nn.CrossEntropyLoss() ## takes logits not probs
        return loss_fn(y_pred, y_target)



class CBOW_Trainer():
    def __init__(self, num_epochs, lr, batch_size, train_data, val_data, device):
        self.num_epochs = num_epochs
        self.lr = lr
        self.batch_size = batch_size
        vocabSize = len(train_data.word_to_id)
        self.train_data = train_data
        self.val_data = val_data
        self.device = device


    def train(self, model):
        optimizer = torch.optim.SGD(model.parameters(), lr=self.lr, momentum=0.9)

        train_loader = DataLoader(self.train_data, batch_size = self.batch_size, shuffle=True) 

        evaluator = CBOW_Evaluator(self.val_data, self.batch_size, self.device)

        for epoch in range(self.num_epochs):
            epoch_loss = 0
            num_batches = 0

            for batch in train_loader:
                X,y_target = batch
                ## Do stuff 
                num_batches+=1

                X,y_target = X.to(self.device), y_target.to(self.device)
                y_pred = model(X)

                loss = model.loss(y_pred, y_target)


                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item()


            if epoch%20 == 0:
                val_loss = round(evaluator.compute_loss(model), 5)

                print(f"Epoch {epoch}:\t Avg Train Loss: {round(epoch_loss/num_batches,5)}\t Avg Val Loss: {val_loss}")


        print('Training done!')
        print(f"Avg Train Loss: {round(epoch_loss/num_batches,5)}")



class CBOW_Evaluator():
    def __init__(self, test_data, batch_size, device):
        self.test_loader = DataLoader(test_data, batch_size = batch_size, shuffle=True)
        self.device=device

    @torch.no_grad()
    def compute_loss(self, model):
        total_loss = 0
        # with torch.no_grad():
        for i, datapoint in enumerate(self.test_loader):
            X,y_target = datapoint
            X,y_target = X.to(self.device), y_target.to(self.device)
            y_pred = model(X)
            loss = model.loss(y_pred, y_target)

            total_loss += loss.item()
        return total_loss/(i+1)


    @torch.no_grad()
    def get_preds(self, model):
        gold = []
        predicted = []
        for i,datapoint in enumerate(self.test_loader):
            X,y_target = datapoint
            X,y_target = X.to(self.device), y_target.to(self.device)
            y_pred = model(X)
            labels = torch.argmax(y_pred, dim=1)

            predicted.extend(labels.cpu())
            gold.extend(y_target.cpu())

        return gold, predicted



        






