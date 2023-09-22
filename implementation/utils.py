# DO NOT CHANGE THIS FILE

def calculate_accuracy(gold, predictions):
    gold = list(gold)
    predictions = list(predictions)
    assert len(gold) == len(predictions), "Gold and system don't have the same number of sentence"

    predictions_ok = []
    for gold_sent, pred_sent in zip(gold, predictions):
        assert len(gold_sent) == len(pred_sent), f"Different number of tokens in sentence:\n{gold_sent}\n{pred_sent}"

        # Skip the dummy tokens
        gold_sent = gold_sent[1:-1]
        pred_sent = pred_sent[1:-1]
        for gold_tok, prediction_tok in zip(gold_sent, pred_sent):
            predictions_ok.append(gold_tok.tag == prediction_tok.tag)

    return (predictions_ok.count(True) / float(len(predictions_ok))) * 100
