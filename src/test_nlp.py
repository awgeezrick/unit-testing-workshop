import unittest
from nlp import remove_stop_words


class TestNlp(unittest.TestCase):
    def test_remove_stop_words_should_remove_a(self):
        self.assertEqual('hello', remove_stop_words('hello a'))

    def test_remove_stop_words_should_remove_the_a_an(self):
        self.assertEqual('hello i am david', remove_stop_words('hello a the an i am david'))