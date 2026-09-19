import unittest

from src.score_calculator import get_rating


class TestScoreCalculator(unittest.TestCase):

    def test_excellent_rating(self):
        self.assertEqual(get_rating(100), "Excellent")
        self.assertEqual(get_rating(90), "Excellent")

    def test_meets_expectations_rating(self):
        self.assertEqual(get_rating(89), "Meets Expectations")
        self.assertEqual(get_rating(80), "Meets Expectations")

    def test_needs_improvement_rating(self):
        self.assertEqual(get_rating(79), "Needs Improvement")
        self.assertEqual(get_rating(70), "Needs Improvement")

    def test_unsatisfactory_rating(self):
        self.assertEqual(get_rating(69), "Unsatisfactory")
        self.assertEqual(get_rating(0), "Unsatisfactory")


if __name__ == "__main__":
    unittest.main()
