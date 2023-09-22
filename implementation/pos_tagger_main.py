# DO NOT CHANGE THIS FILE

import argparse

import corpus
import pos_tagger
import utils


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("PATH_TR",
                        help="Path to train file with POS annotations")
    parser.add_argument("PATH_TE",
                        help="Path to test file (POS tags only used for evaluation)")
    args = parser.parse_args()

    tr_sents = corpus.read_sentences(args.PATH_TR)
    te_sents = corpus.read_sentences(args.PATH_TE, test=True)

    for pos_tagger in [pos_tagger.AlwaysNN, pos_tagger.Majority, pos_tagger.HMM]:
        pos_tagger = pos_tagger(tr_sents)
        for te_path in [args.PATH_TE]:
            # test=True ensures that you do not have access to the gold tags (and inadvertently use them)
            te_instances = corpus.read_sentences(te_path, test=True)
            pos_tagger.tag(te_instances)
            te_gold = corpus.read_sentences(te_path)
            accuracy = utils.calculate_accuracy(te_gold, te_instances)
            print(f"{te_path:15} {pos_tagger.__class__.__name__:15}"
                  f"Accuracy [{len(te_instances):6} sentences]: {accuracy:.3f}")
