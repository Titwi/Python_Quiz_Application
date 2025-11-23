

# Access the quiz_scores list from the Quizarium class
def get_all_scores():
    """Returns all scores stored in the Quizarium class"""
    return Quizarium.quiz_scores

def display_all_scores():
    """Displays all scores in a formatted way"""
    scores = get_all_scores()

    if not scores:
        print("No scores recorded yet.")
        return

    print("\n=== All Quiz Scores ===")
    for i, score in enumerate(scores, 1):
        print(f"\n{i}.")
        print(f"  Name: {score['name']}")
        print(f"  Category: {score['category']}")
        print(f"  Score: {score['score']}/{score['total_questions']}")
        print(f"  Percentage: {score['percentage']:.2f}%")

if __name__ == "__main__":
    display_all_scores()
