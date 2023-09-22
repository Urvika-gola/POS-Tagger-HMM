# DO NOT CHANGE THIS FILE

from implementation import pos_tagger
from implementation.corpus import read_sentences
from implementation import utils

TR = "data/train"
TE = "data/test.ref"
hmm = pos_tagger.HMM(read_sentences(TR))

def get_accuracy(tagger, test):
    te_instances = read_sentences(test, test=True)
    tagger.tag(te_instances)
    return utils.calculate_accuracy(read_sentences(test), te_instances)


hmm_accuracy = get_accuracy(hmm, TE)


def test_hmm_92():
    assert hmm_accuracy >= 92


def test_hmm_93():
    assert hmm_accuracy >= 93


def test_hmm_94():
    assert hmm_accuracy >= 94


def test_hmm_viterbi_matrix():
    assert hmm_accuracy >= 94.142

def test_hmm_95():
    assert hmm_accuracy >= 95


def test_hmm_viterbi_backpointers():
    assert hmm_accuracy >= 95.192

def test_hmm_morphology():
    assert hmm_accuracy >= 95.5


def test_hmm_97():
    assert hmm_accuracy >= 97


# def test_hmm_max():
#     threshold = 100
#     assert hmm_accuracy == pytest.approx(threshold, rel=0.001) or accuracy > threshold
