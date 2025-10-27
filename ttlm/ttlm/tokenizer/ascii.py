import torch

from ttlm.tokenizer.base import Tokenizer

class AsciiTokenizer(Tokenizer):
    """A simple ASCII tokenizer."""

    @property
    def bos_token_id(self) -> int:
        return 128

    @property
    def bos_token(self) -> str:
        return "<BOS>"

    @property
    def eos_token_id(self) -> int:
        return 129

    @property
    def eos_token(self) -> str:
        return "<EOS>"

    @property
    def pad_token_id(self) -> int:
        return 130

    @property
    def pad_token(self) -> str:
        return "<PAD>"

    @property
    def unk_token_id(self) -> int:
        return 131

    @property
    def unk_token(self) -> str:
        return "<UNK>"

    @property
    def vocab_size(self) -> int:
        # 128 ASCII + 4 special tokens
        return 132
    
    def train(self, texts: list[str]) -> None:
        """We don't need to train the tokenizer for ASCII."""
        pass

    def encode(
        self, strings: list[str], bos: bool = True, eos: bool = True
    ) -> list[torch.LongTensor]:
        """Encodes a batch of strings to their ASCII values."""
        encoded = []
        for s in strings:
            tokens = [ord(c) if ord(c) < 128 else self.unk_token_id for c in s]
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
                if token < 128:
                    chars.append(chr(token))
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