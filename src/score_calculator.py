"""
Support QA Score Calculator

Calculates a customer support QA score across five categories
and flags critical errors.
"""

CATEGORIES = {
    "Communication & Professionalism": 20,
    "Understanding the Customer's Issue": 20,
    "Resolution & Accuracy": 30,
    "Process Compliance": 15,
    "Customer Experience": 15,
}


def get_score(category, maximum):
    """Ask for and validate a category score."""
    while True:
        try:
            score = float(input(f"{category} (0-{maximum}): "))

            if 0 <= score <= maximum:
                return score

            print(f"Please enter a score between 0 and {maximum}.")

        except ValueError:
            print("Please enter a valid number.")


def get_rating(score):
    """Return the QA rating for a numerical score."""
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Meets Expectations"
    elif score >= 70:
        return "Needs Improvement"
    else:
        return "Unsatisfactory"


def get_critical_error():
    """Ask whether a critical error was identified."""
    while True:
        answer = input("Critical error identified? (yes/no): ").strip().lower()

        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False

        print("Please enter yes or no.")


def calculate_score():
    """Run an interactive QA evaluation."""
    print("\nSupport QA Score Calculator")
    print("=" * 40)

    scores = {}

    for category, maximum in CATEGORIES.items():
        scores[category] = get_score(category, maximum)

    total_score = sum(scores.values())
    rating = get_rating(total_score)

    print("\nCritical Error Check")
    print("-" * 40)

    critical_error = get_critical_error()

    print("\nQA Evaluation Result")
    print("=" * 40)

    for category, score in scores.items():
        maximum = CATEGORIES[category]
        print(f"{category}: {score:g}/{maximum}")

    print("-" * 40)
    print(f"Final QA Score: {total_score:g}/100")
    print(f"Rating: {rating}")

    if critical_error:
        print("Critical Error: YES")
        print(
            "Result Flag: CRITICAL FAILURE "
            "(apply your organization's critical-error policy)"
        )
    else:
        print("Critical Error: NO")
        print("Result Flag: Standard numerical result")

    print("=" * 40)


if __name__ == "__main__":
    calculate_score()
