import numpy as np

class DRR:
    def __init__(self, path, seq_length):
        self.fp = open(path ,"r")
        self.data = self.fp.read()
        self.chrs = list(set(self.data))
        self.char2 = {ch:i for (i, ch) in enumerate(self.chrs)}
        self.ix2char = {i:ch for (i, ch) in enumerate(self.chrs)}
        self.vocab_size = len(self.chrs)
        self.seq_length = seq_length


seq_length = 25
#read text from the "input.txt" file
data_reader = DRR("sherlock.txt", seq_length)
print(data_reader.vocab_size)
print(data_reader.chrs)