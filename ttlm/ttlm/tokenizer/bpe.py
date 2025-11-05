import torch

from ttlm.tokenizer.base import Tokenizer

def tokenize_text(text, vocab, to_id = False, unk_token_id = None):
    token_sizes = set([len(token) for token in vocab])
    token_sizes = sorted(token_sizes)[::-1]

    tokenized_text = []

    head = 0
    while head < len(text):
        for token_size in token_sizes:
            token_found = False
            if text[head: head+token_size] in vocab:
                if not to_id:
                    tokenized_text.append(text[head: head+token_size])
                else:
                    tokenized_text.append(vocab.index(text[head: head+token_size]))
                head = head + token_size
                token_found = True
                break
        if not token_found:
            if unk_token_id is None:
                raise ValueError("We can't find any matching token!")
            else:
                tokenized_text.append(unk_token_id)
                head += 1
    return tokenized_text

class BPETokenizer(Tokenizer):
    """A BPE tokenizer."""
    
    def __init__(self, vocab = None):
        self.vocab = vocab
        if vocab is None:
            self.vocab = [chr(i) for i in range(128)]

    @property
    def bos_token_id(self) -> int:
        return len(self.vocab)

    @property
    def bos_token(self) -> str:
        return "<BOS>"

    @property
    def eos_token_id(self) -> int:
        return len(self.vocab) + 1

    @property
    def eos_token(self) -> str:
        return "<EOS>"

    @property
    def pad_token_id(self) -> int:
        return len(self.vocab) + 2

    @property
    def pad_token(self) -> str:
        return "<PAD>"

    @property
    def unk_token_id(self) -> int:
        return len(self.vocab) + 3

    @property
    def unk_token(self) -> str:
        return "<UNK>"

    @property
    def vocab_size(self) -> int:
        # 128 ASCII + 4 special tokens
        return len(self.vocab) + 4
    
    def train(self, texts: list[str], num_merges: int) -> None:

        vocab = self.vocab
        addon_vocab = list("".join(texts))
        vocab = list(set(vocab + addon_vocab))
        
        for _ in range(num_merges):
            tokenized_texts = [tokenize_text(text, vocab) for text in texts]
            
            occurence_dict = {}
            for tokenized_text in tokenized_texts:
                for idx in range(len(tokenized_text) - 1):
                    pair = tokenized_text[idx] + tokenized_text[idx+1]
                    if pair not in occurence_dict:
                        occurence_dict[pair] = 0
                    else:
                        occurence_dict[pair] += 1
            
            most_frequent_pair = None
            max_occurence = 0
            for pair,occurence in occurence_dict.items():
                if occurence > max_occurence:
                    max_occurence = occurence
                    most_frequent_pair = pair
                    
            vocab.append(most_frequent_pair)
            
            print(_, "|", most_frequent_pair, "|")

        self.vocab = vocab

    def encode(
        self, strings: list[str], bos: bool = True, eos: bool = True
    ) -> list[torch.LongTensor]:
        """Encodes a batch of strings to their ASCII values."""
        encoded = []
        for s in strings:
            tokens = tokenize_text(s, self.vocab, to_id = True, unk_token_id = self.unk_token_id)
            if bos:
                tokens = [self.bos_token_id] + tokens
            if eos:
                tokens.append(self.eos_token_id)
            encoded.append(torch.tensor(tokens, dtype=torch.long))
        return encoded

    def decode(
        self, tokens: list[list[int]], special_tokens: bool = False
    ) -> list[str]:
        """Decodes a batch of ASCII values to strings."""
        decoded = []
        special_tokens_to_remove = {self.bos_token_id, self.eos_token_id, self.pad_token_id}
        for token_list in tokens:
            if not special_tokens:
                token_list = [t for t in token_list if t not in special_tokens_to_remove]
            chars = []
            for token in token_list:
                if token < len(self.vocab):
                    chars.append(self.vocab(token))
                elif token == self.bos_token_id:
                    chars.append("<BOS>")
                elif token == self.eos_token_id:
                    chars.append("<EOS>")
                elif token == self.unk_token_id:
                    chars.append("<UNK>")
                elif token == self.pad_token_id:
                    chars.append("<PAD>")
            decoded.append("".join(chars))
        return decoded