import unittest
from calculator import add


class TestCalculator(unittest.TestCase):
    def test_add_1_and_1_should_return_2(self):
        self.assertEqual(2, add(1, 1))

# pip install rednose
# nosetests --with-watch --rednose

# remove_stop_words(str) => str_without_stopwords
# the, a, an