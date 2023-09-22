from abc import ABC, abstractmethod
import itertools
import operator
import collections
import re
import math


class POStagger(ABC):
    @abstractmethod
    def __init__(self, sentences):
        pass

    @abstractmethod
    def tag(self, sentences):
        pass


class AlwaysNN(POStagger):
    ## AlwaysNN baseline already implemented
    def __init__(self, sentences):
        self.only_tag = "NN"

    def tag(self, sentences):
        for sentence in sentences:
            for token in sentence:
                token.tag = self.only_tag


class Majority(POStagger):
    def __init__(self, sentences):
        # YOUR CODE GOES HERE
        pass

    def tag(self, sentences):
        # YOUR CODE GOES HERE
        pass


class HMM(POStagger):
    def __init__(self, sentences):
        # YOUR CODE GOES HERE
        pass


    def tag(self, sentences):
        # YOUR CODE GOES HERE
        pass
