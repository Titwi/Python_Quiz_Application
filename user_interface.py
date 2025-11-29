
from databases.quiz_database import quiz_questions #Imports the content of the quiz_database.py file

import random # Imports the random module
import json # Imports the json module for saving and loading data

# An empty list where all user scores will be stored
quiz_scores = []

# Function to load scores from file at startup
def load_scores_from_file(filename="quiz_scores.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Function to save scores to JSON file (for persistent storage)
def save_scores_to_json(filename="quiz_scores.json"):
    with open(filename, "w") as f:
        json.dump(quiz_scores, f, indent=2)

# Function to get the name of the player in a string format
def get_name():
    while True: #Loop to ask the player to enter their username
        user_name = input("Please, type your username: ")

        # triggers if the user doesn't enter anything or only enters spaces
        if not user_name or not user_name.strip():
            print("You haven't answered yet...")

        # triggers when username has been entered correctly
        else:
            print("Nice to meet you, " + user_name + "!")
            return user_name


### Now the player is shown four categories, which are included in the quiz_questions dictionary, and chooses one ###

#Function shows the available categories and returns the one chosen by the player
def choose_category(topics):
    categories = list(topics)
    print("\n These are the available categories for the quiz:")
    for i, category in enumerate(categories, start=1): # Each category is shown with a unique selectable number
        print(f"{i}. {category}")

    while True: #Loop to ask the player to choose a category
        selection = input("What category would you like to be challenged with today? " #After being shown the categories, the player is asked to choose one
                          f"Please enter the category number (1-{len(categories)}) ")

        # Triggers if the player doesn't enter anything or only enters spaces
        if not selection or not selection.strip():
            print("You haven't chosen a category yet...")

        # Triggers if the player enters a number within the range of the categories
        elif selection.isdigit() and 1 <= int(selection) <= len(categories):
            return categories[int(selection) - 1]

        # Triggers if the player enters a number outside the range of the categories
        else:
            print("That number does not correspond to any of the available categories.")
### Afterward, the player is asked how many questions they want to answer for the chosen category,
    ## and the questions are randomly selected from quiz_questions ###

# Function to ask the player how many questions they want to answer for the chosen category
def number_of_questions(selected_category):
    total_questions = len(selected_category)
    while True: # Loop to ask the player how many questions the user wants to answer
        chosen_number_questions = input(f"There are {total_questions} questions available for this category. "
          f"How many would you like to answer? (Please enter a number between 1 and " + str(total_questions) + ") ")
        if not chosen_number_questions: #
            print("You haven't answered yet...")
        elif chosen_number_questions.isdigit() and 1 <= int(chosen_number_questions) <= total_questions: # Triggers if the player enters a number within the range of the questions
            return int(chosen_number_questions)
        else: # Triggers if the player enters a number outside the range of the questions
            print("That value is not within the stated range.")

# Function to randomise the number of questions chosen from the selected category
def random_questions(questions, quantity):
    randomise_questions = random.sample(questions, quantity)
    return randomise_questions


### Then, the questions are displayed to the player ###

# Function to display the questions, and answer options to the player
def quiz_questions_and_answers(quiz):
    score = 0
    for question in quiz: # Loop to display the specified number of questions and answer options to the player
        print(f"\nQuestion: {question['question']}")

        # The order of answer options displayed is randomised
        shuffled_options = question['options'].copy()
        random.shuffle(shuffled_options)

        for i, option in enumerate(shuffled_options, start=1): # Each answer option is shown with a unique selectable number
            print(f"{i}. {option}")

        while True:
            answer = input("Your answer: ")
            if not answer or not answer.strip():  # Triggers if the player doesn't enter anything or only enters spaces
                print("You haven't answered yet... Please enter your answer.")
            elif answer.isdigit() and 1 <= int(answer) <= len(shuffled_options):  # Triggers if the player enters a number within the range of the answer options
                if shuffled_options[int(answer) - 1] == question['correct_answer']:  # Triggers if the player's answer is correct'
                    print("Correct!")
                    score += 1
                else:  # Triggers if the player's answer is incorrect
                    print(f"Wrong! The correct answer is {question['correct_answer']}.")
                break  # Exit the while loop after a valid answer
            else:  # Triggers if the player enters a number outside the range of the answer options
                print("That answer does not correspond to any of the stated options. Please enter a number between 1 and " + str(len(shuffled_options)) + "")
    return score

# Function initialising the quiz by guiding the user through and calling related functions in the specific order
def play_quiz(player_name=None):

    # If no player name is provided, show the introduction and get name
    if player_name is None:
        # A quick introduction of what is Quizarium (only shown on first user play)
        print("Hello there, and welcome to the Quizarium! A quiz where you can demonstrate your knowledge in your preferred topic.")
        print("  Here are some instructions:")
        print("   - Your score will be based on how many questions you answer correctly out of the total number of questions available per chosen category.")
        print("   - Your username will be saved and you'll be able to view your scores at any time. However, if you end the quiz session and decide to play again later, you must choose a new username.")

        # Calls the function to get the name of the player
        player_name = get_name()
    else:
        print(f"\nWelcome back, {player_name}!")

    # Calls the function using, as a parameter, the keys of the dictionary
    player_chosen_category = choose_category(quiz_questions.keys())
    print(f"\nLet's see how good you are in {player_chosen_category}...")

    # Calls the function using as a parameter the questions of the category chosen by the player
    player_number_of_questions = number_of_questions(quiz_questions[player_chosen_category])

    # Calls the function using as parameters the questions of the category chosen by the player and the number of questions chosen by the player
    player_random_questions = random_questions(quiz_questions[player_chosen_category], player_number_of_questions)

    # Calls the function using as parameter the randomised questions of the category chosen by the player
    player_score = quiz_questions_and_answers(player_random_questions)

    #Show the final score to the player
    print(player_name, "your final score is: " , player_score)
    print("That makes a overall score of ", player_score/player_number_of_questions*100, "%")

    # Store score in the list
    quiz_scores.append({
        'name': player_name,
        'category': player_chosen_category,
        'score': player_score,
        'total_questions': player_number_of_questions,
        'percentage': player_score/player_number_of_questions*100
    })
    # Save to JSON file immediately to persist data
    save_scores_to_json()
    print("Your score has been saved.")

    # Display top 3 scores for the category just played
    display_top_overall_scores(player_chosen_category, 3)

    # Return the player name for reuse
    return player_name

# Function to handle Yes/no answers
def yes_no_answer(question):
    while True:
        answer = input(question)
        if answer == "Y" or answer == "y":
            return True
        elif answer == "N" or answer == "n":
            return False
        else:
            print("Please enter Y or N. ")

#Function that saves all scores to a text file organised by category
def save_scores_to_file(filename="quiz_scores.txt"):
   # Group scores by category
    scores_by_category = {}
    for score in quiz_scores:
        category = score['category']
        if category not in scores_by_category:
            scores_by_category[category] = []
        scores_by_category[category].append(score)

    # Write to file
    with open(filename, "w") as f:
        f.write("=" * 80 + "\n")
        f.write("QUIZARIUM - ALL SCORES\n")
        f.write("=" * 80 + "\n\n")

        for category, scores in scores_by_category.items():
            f.write(f"\n{'=' * 80}\n")
            f.write(f"CATEGORY: {category}\n")
            f.write(f"{'=' * 80}\n\n")

            # Sort by percentage (descending), then by total_questions (descending)
            sorted_scores = sorted(scores, key=lambda x: (x['percentage'], x['total_questions']), reverse=True)

            # 1. Display top 3 player scores
            f.write("TOP 3 PLAYER SCORES:\n")
            f.write("-" * 80 + "\n")
            f.write(f"{'Rank':<6} {'Name':<20} {'Score':<15} {'Percentage':<10}\n")
            f.write("-" * 80 + "\n")

            top_3 = sorted_scores[:3]
            for i, score in enumerate(top_3, 1):
                score_str = f"{score['score']}/{score['total_questions']}"
                percentage_str = f"{score['percentage']:.2f}%"
                f.write(f"{i:<6} {score['name']:<20} {score_str:<15} {percentage_str:<10}\n")

            # 2. Display average score for the category
            f.write("\n")
            f.write("AVERAGE SCORE:\n")
            f.write("-" * 80 + "\n")
            avg_percentage = sum(s['percentage'] for s in scores) / len(scores)
            f.write(f"Average across all players: {avg_percentage:.2f}%\n")

            # 3. Display all player scores
            f.write("\n")
            f.write("ALL PLAYER SCORES:\n")
            f.write("-" * 80 + "\n")
            f.write(f"{'Rank':<6} {'Name':<20} {'Score':<15} {'Percentage':<10}\n")
            f.write("-" * 80 + "\n")

            for i, score in enumerate(sorted_scores, 1):
                score_str = f"{score['score']}/{score['total_questions']}"
                percentage_str = f"{score['percentage']:.2f}%"
                f.write(f"{i:<6} {score['name']:<20} {score_str:<15} {percentage_str:<10}\n")

    print(f"\nScores have been saved to {filename}")

#Function displaying the contents of the saved scores file
def display_file_contents(filename="quiz_scores.txt"):
    try:
        with open(filename, "r") as f:
            print("\n" + "=" * 80)
            print("SCORES FILE CONTENT:")
            print("=" * 80)
            print(f.read())
    except FileNotFoundError:
        print(f"\nFile {filename} not found.")

#  Function displaying the top 3 scores for a specific category
def display_top_overall_scores(category, limit=3):

    if not quiz_scores:
        print("No scores recorded for category ", category  ," yet.")
        return

    # Filter scores by the specific category
    category_scores = [score for score in quiz_scores if score['category'] == category]

    if not category_scores:
        print(f"No scores recorded yet for {category}.")
        return

    # Sort by percentage (descending), then by total_questions (descending)
    sorted_scores = sorted(category_scores, key=lambda x: (x['percentage'], x['total_questions']), reverse=True)
    display_count = min(limit, len(sorted_scores))

    print(f"\n=== Top {display_count} Score(s) for {category} ===")
    for i in range(display_count):
        score = sorted_scores[i]
        print(f"\n{i+1}.")
        print(f"  Name: {score['name']}")
        print(f"  Score: {score['score']}/{score['total_questions']}")
        print(f"  Percentage: {score['percentage']:.2f}%")

# Function displaying the top 3 scores per category sorted by percentage
def display_top_scores_per_category(limit=3):
    if not quiz_scores:
        print("No scores recorded yet.")
        return

    # Group scores by category
    scores_by_category = {}
    for score in quiz_scores:
        category = score['category']
        if category not in scores_by_category:
            scores_by_category[category] = []
        scores_by_category[category].append(score)

    # Display top scores for each category
    print(f"\n=== Top {limit} Score(s) Per Category ===")
    for category, scores in scores_by_category.items():
        # Sort by percentage (descending), then by total_questions (descending)
        sorted_scores = sorted(scores, key=lambda x: (x['percentage'], x['total_questions']), reverse=True)
        display_count = min(limit, len(sorted_scores))

        print(f"\n{category}:")
        for i in range(display_count):
            score = sorted_scores[i]
            print(f"  {i+1}. {score['name']} - {score['score']}/{score['total_questions']} ({score['percentage']:.2f}%)")

# Function displaying all scores sorted by percentage (highest to lowest)
def display_all_scores():
    if not quiz_scores:
        print("No scores recorded yet.")
        return

    # Sort by percentage (descending), then by total_questions (descending)
    sorted_scores = sorted(quiz_scores, key=lambda x: (x['percentage'], x['total_questions']), reverse=True)

    print("\n=== All Quiz Scores (Highest to lowest) ===")
    for i, score in enumerate(sorted_scores, 1):
        print(f"\n{i}.")
        print(f"  Name: {score['name']}")
        print(f"  Category: {score['category']}")
        print(f"  Score: {score['score']}/{score['total_questions']}")
        print(f"  Percentage: {score['percentage']:.2f}%")

# Function that loops the quiz game until the user decides to stop and/or no more users want to play
def run():
    global quiz_scores
    # Load existing scores from file at startup
    quiz_scores = load_scores_from_file()
    if quiz_scores:
        print(f"Loaded {len(quiz_scores)} existing score(s) from previous sessions.")

    keep_playing = True
    current_player = None

    while keep_playing:
        # Play quiz with current player name (None for first play)
        current_player = play_quiz(current_player)

        continue_playing = yes_no_answer("Would you like to play another quiz? (Please enter Y for Yes and N for No). ")
        if not continue_playing:
            # Reset player name for next player
            current_player = None
            continue_playing_2 = yes_no_answer("Does anybody else want to play? (Please enter Y for Yes and N for No) ")
            if not continue_playing_2:
                keep_playing = False
                # Display top 3 scores per category when everyone is done
                display_top_scores_per_category(3)
                # Save all scores to file
                save_scores_to_file()
                # Display the contents of the file
                display_file_contents("quiz_scores.txt")
                print("\nThank you for playing Quizarium! See you soon!")
            else:
                continue
        else:
            continue

# Initialises the quiz game by calling the run function
if __name__ == "__main__":
    run()