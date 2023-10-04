from abc import ABC, abstractmethod
import operator
import collections
import re


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
        self.dict_word_and_tag = collections.defaultdict(lambda: collections.defaultdict(int))
        self.popular_tags = {}
        # Calculate word tag dict
        for sent in sentences:
            for token in sent:
                word = token.word
                tag = token.tag
                self.dict_word_and_tag[word][tag] += 1
        # Identify the most common tag for each word
        for word, tags in self.dict_word_and_tag.items():
            self.popular_tags[word] = max(tags.items(), key=operator.itemgetter(1))[0]

    def tag(self, sentences):
        for sent in sentences:
            for t in sent:
                t.tag = self.popular_tags.get(t.word, "NN")  # Default is "NN" tag for words which are unseen


class HMM(POStagger):
    def __init__(self, sentences):
        self.likelihood = collections.defaultdict(lambda: collections.defaultdict(float))
        self.predicted = collections.defaultdict(lambda: collections.defaultdict(float))
        self.tags = list(set(token.tag for sentence in sentences for token in sentence))
        self.words = list(set(token.word for sentence in sentences for token in sentence))
        self.tag2id = {tag: i for i, tag in enumerate(self.tags)}
        self.word2id = {word: i for i, word in enumerate(self.words)}
        counting_of_tags = collections.defaultdict(int)
        # Calculate likelihood and predicted probs
        for s in sentences:
            for val, token in enumerate(s):
                word, tag = token.word, token.tag
                counting_of_tags[tag] += 1
                if val == 0:
                    previous_tag = "<s>"
                else:
                    previous_tag = s[val - 1].tag
                self.likelihood[previous_tag][tag] += 1
                self.predicted[tag][word] += 1

        for previous_tag in self.likelihood:
            # Laplace smoothing to likelihood probabilities
            for t in self.tags:
                self.likelihood[previous_tag][t] += 1
                self.likelihood[previous_tag][t] /= (counting_of_tags[previous_tag] + len(self.tags))

        # Normalization
        for t, word_counts in self.predicted.items():
            sum_ = sum(word_counts.values())
            for word, count in word_counts.items():
                self.predicted[t][word] = count / sum_

    def guess_tag(self, token):
        pos = "NN"
        if re.match(r'.*ly$', token):
            pos = "RB"
        elif re.match(r'.*ing$', token):
            pos = "VBG"
        elif re.match(r'.*ed$', token):
            pos = "VBD"
        elif token[0].isupper():
            pos = "NNP"
        elif re.match(r'^-?\d+(\.\d+)?$', token):  # Numbers integers or decimals
            pos = "CD"
        elif re.match(r'\d+%$', token) or re.match(r'\$\d+', token):  # Percentages or amount
            pos = "CD"
        elif token == ",":  # comma
            pos = ","
        elif token == ".":
            pos = "."
        elif re.match(r'^[A-Z]{2,}$', token):  # All uppercase tokens (e.g., "US", "UK")
            pos = "NNP"
        elif re.match(r'.*-.*', token):  # Hyphen words (e.g., "pianist-comedian")
            pos = "JJ"
        elif token.lower() in ["yet", "and", "but", "or"]:
            pos = "CC"
        elif token.lower() in ["the", "a", "an"]:
            pos = "DT"
        elif token.lower() in ["is", "am", "are", "was", "were", "has", "have", "had"]:
            pos = "VB"
        return pos

    def tag(self, sentences):
        for s in sentences:
            w = [token.word for token in s]
            best_tags = self.viterbi(w)
            for i, token in enumerate(s):
                token.tag = best_tags[i]

    def viterbi(self, words):
        V = [{} for _ in words]
        path = {}
        # init
        for tag in self.tags:
            V[0][tag] = self.likelihood["<s>"].get(tag, 0) * self.predicted[tag].get(words[0], 1.0 / len(self.words))
            path[tag] = [tag]
        # Iterate over words
        for t in range(1, len(words)):
            updated_path = {}
            for tag in self.tags:
                if words[t] not in self.word2id:
                    guessed_tag = self.guess_tag(words[t])
                    emission_prob = 1.0 if tag == guessed_tag else 0.0
                else:
                    emission_prob = self.predicted[tag].get(words[t], 0)
                max_prob, prev_st = max(
                    (V[t - 1][previous_tag] * self.likelihood[previous_tag].get(tag, 0) * emission_prob, previous_tag) for
                    previous_tag in self.tags)
                V[t][tag] = max_prob
                updated_path[tag] = path[prev_st] + [tag]
            path = updated_path
        _, best_tag_sequence = max((V[len(words) - 1][tag], tag) for tag in self.tags)
        return path[best_tag_sequence]
