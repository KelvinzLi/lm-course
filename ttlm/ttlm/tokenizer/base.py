import abc

import torch

class Tokenizer(abc.ABC):
    """Abstract base class for tokenizers."""

    @property
    @abc.abstractmethod
    def bos_token_id(self) -> int:
        """Beginning of sentence token id."""
        pass

    @property
    @abc.abstractmethod
    def bos_token(self) -> str:
        """Beginning of sentence token string."""
        pass

    @property
    @abc.abstractmethod
    def eos_token_id(self) -> int:
        """End of sentence token id."""
        pass

    @property
    @abc.abstractmethod
    def eos_token(self) -> str:
        """End of sentence token string."""
        pass

    @property
    @abc.abstractmethod
    def pad_token_id(self) -> int:
        """Padding token id."""
        pass

    @property
    @abc.abstractmethod
    def pad_token(self) -> str:
        """Padding token string."""
        pass

    @property
    @abc.abstractmethod
    def unk_token_id(self) -> int:
        """Unknown token id."""
        pass

    @property
    @abc.abstractmethod
    def unk_token(self) -> str:
        """Unknown token string."""
        pass

    @property
    @abc.abstractmethod
    def vocab_size(self) -> int:
        """Returns the size of the vocabulary."""
        pass
    
    @abc.abstractmethod
    def train(self, texts: list[str]) -> None:
        """Trains the tokenizer on a list of texts."""
        pass

    @abc.abstractmethod
    def encode(
        self, strings: list[str], bos: bool = True, eos: bool = True
    ) -> list[torch.LongTensor]:
        """Encodes a batch of strings."""
        pass

    @abc.abstractmethod
    def decode(
        self, tokens: list[list[int]], special_tokens: bool = False
    ) -> list[str]:
        """Decodes a batch of tokens.
        When special_tokens=True, special tokens should be decoded as:
        - BOS token: <BOS>
        - EOS token: <EOS>
        - UNK token: <UNK>
        - PAD token: <PAD>
        """
        pass
