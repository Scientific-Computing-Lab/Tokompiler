from typing import List
from abc import ABC, abstractmethod


class Tokenizer(ABC):

    @abstractmethod
    def tokenize(self, s: str) -> List[str]:
        '''
            convert string into sequence tokens

            Parameters:
                s: str -  input string to be tokenized
            Result:
                convert string into list of tokens
        '''
        pass

    @abstractmethod
    def encode(self, s: str, ignore_case: bool = True) ->  List[int]:
        '''
            encode given string to ids

            Parameters:
                s: String - input string to be tokenized
                lang: String - programming language of @param:s
                ignore_case: bool - whether to ignore case

            Result:
                list of token ids
        '''
        pass

    @abstractmethod
    def decode(self, t: List[int]) -> str:
        '''
            decode token ids to string

            Parameters:
                t: List[int] -  list of tokens ids

            Results:
                string represents the list of ids

        '''
        pass


class Tokompiler(Tokenizer):
    '''
        Compiler oriented tokenization
    '''
    def __init__(self, vocab_path):
        with open(vocab_path, 'r') as f:
            tokens = [token[:-1] for token in f.readlines()]

        self.special_tokens = ['[PAD]', '[SOS]', '[EOS]', '[UNK]', '[MSK]', '[SEP]', '[CLS]']

        with open(vocab_path, 'r') as f:
            tokens = ['[PAD]', '[SOS]', '[EOS]', '[UNK]', '[MSK]', '[SEP]', '[CLS]'] + tokens

        self.encoder = {token:idx for idx, token in enumerate(tokens, start=1)}
        self.decoder = {val:key for key, val in self.encoder.items()}

    def tokenize(self, s: str, ignore_case: bool = True) -> List[str]:
        return (s.lower() if ignore_case else s).split()

    def encode(self, s: str) ->  List[int]:
        tokens = self.tokenize(s)
        ids = [self.encoder[token] if token in self.encoder else self.encoder['[UNK]'] for token in tokens]

        return ids

    def decode(self, t: List[int]) -> str:
        tokens = ' '.join([self.decoder[id] for id in t])

        return tokens
