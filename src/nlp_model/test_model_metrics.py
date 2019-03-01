import unittest
from src.nlp_model.utils import load_reviews, extract_texts_and_labels
from src.nlp_model.train import train_model
from sklearn.metrics import precision_score, recall_score


class TestModelMetrics(unittest.TestCase):
    def setUp(self):
        reviews = load_reviews('./data/review_100_samples.json')
        texts, labels = extract_texts_and_labels(reviews)

        model, data_val, labels_val = train_model(texts, labels)
        self.y_pred = model.predict(data_val)
        self.y_true = labels_val

    def test_precision_score_should_be_above_threshold(self):
        p = precision_score(self.y_true, self.y_pred)

        self.assertGreaterEqual(p, 0.5)

    def test_recall_score_should_be_above_threshold(self):
        r = recall_score(self.y_true, self.y_pred)

        self.assertGreaterEqual(r, 0.5)
