# DO NOT CHANGE THIS FILE

import argparse


class Token:
    def __init__(self, word, tag):
        self.word = word
        self.tag = tag

    def __str__(self):
        return f"{self.word}/{self.tag}"


def read_sentences(file, max_sents=-1, test=False):
    with open(file) as f:
        sentences = []
        for sent_i, line in enumerate(f.readlines()):
            if sent_i >= max_sents > 0:
                break
            line = line.rstrip()
            tokens = line.split()
            sentence = [Token('<s>', '<s>')]
            for token in tokens:
                # if no tag available or we are testing, use UNK tag
                try:
                    word, tag = token.rsplit('/', 1)
                except ValueError:
                    word = token
                    tag = 'UNK'
                if test:
                    tag = 'UNK'
                sentence.append(Token(word, tag))
            sentence.append(Token('</s>', '</s>'))
            sentences.append(sentence)

        return sentences


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("PATH",
                        help="Path to file with POS annotations")
    parser.add_argument("-m", "--max_sents", type=int, default=-1)
    args = parser.parse_args()

    for i, s in enumerate(read_sentences(args.PATH, args.max_sents)):
        print(f"{i}: {' '.join(map(str, s))}")
