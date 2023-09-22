# DO NOT CHANGE THIS FILE

import pytest

from implementation import pos_tagger
from implementation.corpus import read_sentences
from implementation import utils

TR = "data/train"
TE = "data/test.ref"
always_nn = pos_tagger.AlwaysNN(read_sentences(TR))
majority = pos_tagger.Majority(read_sentences(TR))


def get_accuracy(tagger, test):
    te_instances = read_sentences(test, test=True)
    tagger.tag(te_instances)
    return utils.calculate_accuracy(read_sentences(test), te_instances)


def test_always_nn():
    accuracy = get_accuracy(always_nn, TE)
    threshold = 13.970
    assert accuracy == pytest.approx(threshold, rel=0.001) or accuracy > threshold


def test_majority_89():
    assert get_accuracy(majority, TE) >= 89


def test_majority_90():
    assert get_accuracy(majority, TE) >= 90


def test_majority_91():
    assert get_accuracy(majority, TE) >= 91


def test_majority_92():
    assert get_accuracy(majority, TE) >= 92


def test_majority_max():
    accuracy = get_accuracy(majority, TE)
    threshold = 92.232
    assert accuracy == pytest.approx(threshold, rel=0.001)
