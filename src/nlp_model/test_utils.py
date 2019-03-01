import unittest
from src.nlp_model.utils import load_reviews, extract_texts_and_labels

class TestUtils(unittest.TestCase):
    def test_load_reviews_should_return_list_of_reviews(self):
        reviews = load_reviews('./data/review_100_samples.json')

        self.assertEqual(100, len(reviews))

        self.assertIn('text', list(reviews[0].keys()))
        self.assertIn('stars', list(reviews[0].keys()))

    def test_extract_texts_and_labels(self):
        reviews = [{
            'text': 'this is great',
            'stars': 4
        }, {
            'text': 'this succckss!',
            'stars': 1
        }]
        texts, labels = extract_texts_and_labels(reviews)

        self.assertEqual(['this is great', 'this succckss!'], texts)
        self.assertEqual([1, 0], labels)