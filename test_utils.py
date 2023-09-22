# DO NOT CHANGE THIS FILE

import pytest

from implementation.corpus import Token
from implementation import utils


def test_accuracy():
    doc1 = [[Token("<s>", "<s>"), Token("a", "a"), Token("b", "b"), Token("c", "c"), Token("</s>", "</s>")]]
    doc2 = [[Token("<s>", "<s>"), Token("a", "a"), Token("b", "b"), Token("c", "a"), Token("</s>", "</s>")]]
    accuracy = utils.calculate_accuracy(doc1, doc2)
    assert accuracy == pytest.approx(66.66, rel=0.001)


def test_accuracy_dummy_tokens():
    ## dummy tokens (<s> and </s> do not count
    doc1 = [[Token("<s>", "<s>"), Token("a", "a"), Token("b", "b"), Token("c", "c"), Token("</s>", "</s>")]]
    doc2 = [[Token("<s>", "BLA"), Token("a", "a"), Token("b", "b"), Token("c", "a"), Token("</s>", "BLAH")]]
    accuracy = utils.calculate_accuracy(doc1, doc2)
    assert accuracy == pytest.approx(66.66, rel=0.001)


def test_accuracy_dummy_tokens_multiple_sentences():
    ## dummy tokens (<s> and </s> do not count
    doc1 = [[Token("<s>", "<s>"), Token("a", "a"), Token("b", "b"), Token("c", "c"), Token("</s>", "</s>")],
            [Token("<s>", "<s>"), Token("a", "a"), Token("b", "b"), Token("c", "c"), Token("</s>", "</s>")]]
    doc2 = [[Token("<s>", "BLA"), Token("a", "a"), Token("b", "b"), Token("c", "a"), Token("</s>", "BLAH")],
            [Token("<s>", "BLA"), Token("a", "a"), Token("b", "b"), Token("c", "a"), Token("</s>", "BLAH")]]
    accuracy = utils.calculate_accuracy(doc1, doc2)
    assert accuracy == pytest.approx(66.66, rel=0.001)


def test_accuracy_zero():
    doc1 = [[Token("<s>", "<s>"), Token("a", "a"), Token("b", "b"), Token("c", "c"), Token("</s>", "</s>")]]
    doc2 = [[Token("<s>", "<s>"), Token("a", "b"), Token("b", "c"), Token("c", "a"), Token("</s>", "</s>")]]
    accuracy = utils.calculate_accuracy(doc1, doc2)
    assert accuracy == pytest.approx(0.0, rel=0.001)


def test_accuracy_one():
    doc1 = [[Token("<s>", "<s>"), Token("a", "a"), Token("b", "b"), Token("c", "c"), Token("</s>", "</s>")]]
    doc2 = [[Token("<s>", "<s>"), Token("a", "a"), Token("b", "b"), Token("c", "c"), Token("</s>", "</s>")]]
    accuracy = utils.calculate_accuracy(doc1, doc2)
    assert accuracy == pytest.approx(100, rel=0.001)
