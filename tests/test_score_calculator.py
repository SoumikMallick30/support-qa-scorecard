import unittest

from src.score_calculator import (
    CATEGORIES,
    evaluate_scores,
    get_rating,
    validate_score,
)


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

    def test_validates_category_score_range(self):
        category = "Process Compliance"

        self.assertEqual(validate_score(category, 15), 15)

        with self.assertRaises(ValueError):
            validate_score(category, 16)

        with self.assertRaises(ValueError):
            validate_score(category, -1)

    def test_evaluates_scores_without_critical_error(self):
        evaluation = evaluate_scores(CATEGORIES)

        self.assertEqual(evaluation["total_score"], 100)
        self.assertEqual(evaluation["rating"], "Excellent")
        self.assertFalse(evaluation["critical_error"])
        self.assertEqual(evaluation["result_flag"], "Standard numerical result")

    def test_evaluates_scores_with_critical_error(self):
        scores = {
            "Communication & Professionalism": 18,
            "Understanding the Customer's Issue": 17,
            "Resolution & Accuracy": 24,
            "Process Compliance": 12,
            "Customer Experience": 12,
        }

        evaluation = evaluate_scores(scores, critical_error=True)

        self.assertEqual(evaluation["total_score"], 83)
        self.assertEqual(evaluation["rating"], "Meets Expectations")
        self.assertTrue(evaluation["critical_error"])
        self.assertEqual(evaluation["result_flag"], "CRITICAL FAILURE")

    def test_rejects_missing_category_score(self):
        incomplete_scores = dict(CATEGORIES)
        incomplete_scores.pop("Customer Experience")

        with self.assertRaises(ValueError):
            evaluate_scores(incomplete_scores)


if __name__ == "__main__":
    unittest.main()
