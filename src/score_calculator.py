"""
Support QA Score Calculator

Calculates a customer support QA score across five categories
and flags critical errors.
"""

import argparse


CATEGORIES = {
    "Communication & Professionalism": 20,
    "Understanding the Customer's Issue": 20,
    "Resolution & Accuracy": 30,
    "Process Compliance": 15,
    "Customer Experience": 15,
}

SCORE_ARGUMENTS = {
    "communication": "Communication & Professionalism",
    "understanding": "Understanding the Customer's Issue",
    "resolution": "Resolution & Accuracy",
    "compliance": "Process Compliance",
    "experience": "Customer Experience",
}


def validate_score(category, score):
    """Validate a category score and return it as a float."""
    maximum = CATEGORIES[category]
    score = float(score)

    if not 0 <= score <= maximum:
        raise ValueError(f"{category} must be between 0 and {maximum}.")

    return score


def get_score(category, maximum):
    """Ask for and validate a category score."""
    while True:
        try:
            return validate_score(category, input(f"{category} (0-{maximum}): "))
        except ValueError:
            print(f"Please enter a valid number between 0 and {maximum}.")


def get_rating(score):
    """Return the QA rating for a numerical score."""
    if score >= 90:
        return "Excellent"
    if score >= 80:
        return "Meets Expectations"
    if score >= 70:
        return "Needs Improvement"
    return "Unsatisfactory"


def get_critical_error():
    """Ask whether a critical error was identified."""
    while True:
        answer = input("Critical error identified? (yes/no): ").strip().lower()

        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False

        print("Please enter yes or no.")


def evaluate_scores(scores, critical_error=False):
    """Return a structured QA evaluation from category scores."""
    validated_scores = {}

    for category in CATEGORIES:
        if category not in scores:
            raise ValueError(f"Missing score for {category}.")

        validated_scores[category] = validate_score(category, scores[category])

    total_score = sum(validated_scores.values())
    rating = get_rating(total_score)
    result_flag = (
        "CRITICAL FAILURE"
        if critical_error
        else "Standard numerical result"
    )

    return {
        "scores": validated_scores,
        "total_score": total_score,
        "rating": rating,
        "critical_error": bool(critical_error),
        "result_flag": result_flag,
    }


def print_evaluation(evaluation):
    """Print a QA evaluation result."""
    print("\nQA Evaluation Result")
    print("=" * 40)

    for category, score in evaluation["scores"].items():
        maximum = CATEGORIES[category]
        print(f"{category}: {score:g}/{maximum}")

    print("-" * 40)
    print(f"Final QA Score: {evaluation['total_score']:g}/100")
    print(f"Rating: {evaluation['rating']}")

    if evaluation["critical_error"]:
        print("Critical Error: YES")
        print(
            "Result Flag: CRITICAL FAILURE "
            "(apply your organization's critical-error policy)"
        )
    else:
        print("Critical Error: NO")
        print("Result Flag: Standard numerical result")

    print("=" * 40)


def calculate_score():
    """Run an interactive QA evaluation."""
    print("\nSupport QA Score Calculator")
    print("=" * 40)

    scores = {}

    for category, maximum in CATEGORIES.items():
        scores[category] = get_score(category, maximum)

    print("\nCritical Error Check")
    print("-" * 40)

    evaluation = evaluate_scores(scores, get_critical_error())
    print_evaluation(evaluation)
    return evaluation


def parse_args():
    """Parse optional command-line scores for a non-interactive evaluation."""
    parser = argparse.ArgumentParser(
        description="Calculate a support QA score from category scores."
    )

    for argument_name, category in SCORE_ARGUMENTS.items():
        parser.add_argument(
            f"--{argument_name}",
            type=float,
            help=f"{category} score, max {CATEGORIES[category]}",
        )

    parser.add_argument(
        "--critical-error",
        action="store_true",
        help="Flag the evaluation as a critical failure.",
    )

    return parser.parse_args()


def main():
    """Run either a scripted or interactive QA evaluation."""
    args = parse_args()
    provided_scores = {
        category_name: getattr(args, argument_name)
        for argument_name, category_name in SCORE_ARGUMENTS.items()
    }

    if all(score is None for score in provided_scores.values()):
        calculate_score()
        return

    if any(score is None for score in provided_scores.values()):
        missing = [
            argument_name
            for argument_name, category in SCORE_ARGUMENTS.items()
            if provided_scores[category] is None
        ]
        raise SystemExit(
            "Missing required score arguments for non-interactive mode: "
            + ", ".join(f"--{name}" for name in missing)
        )

    evaluation = evaluate_scores(provided_scores, args.critical_error)
    print_evaluation(evaluation)


if __name__ == "__main__":
    main()
