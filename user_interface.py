
def get_name (): #function to get the name of the player in a string format
    while True:
        name = input("What is your name? ")

        # triggers if the user doesn't enter anything
        if not name:
            print("You haven't answered yet...")

        # triggers if the user enters something other than letters
        elif not all(ch.isalpha() or ch in " -'" for ch in name):
            print("Please enter your name using letters only (no numbers or symbols).")

        # triggers when name has been entered correctly
        else:
            print("Nice to meet you, " + name + "!")
            return name


#Imports the content of the quiz_database.py file
from databases.quiz_database import quiz_questions


#Now the player is shown four categories, which are included in the quiz_questions dictionary, and chooses one

def choose_category(topics): #Function shows the available categories and returns the one chosen by the player
    categories = list(topics)
    print("\n These are the available categories for the quiz:")
    for i, category in enumerate(categories, start=1): # Each category is shown with a unique selectable number
        print(f"{i}. {category}")

    while True:
        selection = input("What category would you like to be challenged with today? " #After being shown the categories, the player is asked to choose one
                          f"Please enter the category number (1-{len(categories)}) ")

        # Triggers if the player doesn't enter anything
        if not selection:
            print("You haven't chosen a category yet...")

        # Triggers if the player enters a number within the range of the categories
        elif selection.isdigit() and 1 <= int(selection) <= len(categories):
            return categories[int(selection) - 1]

        # Triggers if the player enters a number outside the range of the categories
        else:
            print("That number does not correspond to any of the available categories.")





def number_of_questions(selected_category): # Function to ask the player how many questions they want to answer
    total_questions = len(selected_category)
    while True: # Loop to ask the player how many questions they want to answer
        chosen_number_questions = input(f"There are {total_questions} questions available for this category. "
          f"How many would you like to answer? (Please enter a number between 1 and " + str(total_questions) + ") ")
        if not chosen_number_questions: #
            print("You haven't answered yet...")
        elif chosen_number_questions.isdigit() and 1 <= int(chosen_number_questions) <= total_questions: # Triggers if the player enters a number within the range of the questions
            return int(chosen_number_questions)
        else: # Triggers if the player enters a number outside the range of the questions
            print("That value is not within the stated range.")



def random_questions(questions, quantity): # Function to select random questions from the selected category
    import random
    randomise_questions = random.sample(questions, quantity)
    return randomise_questions




# Then, the questions are displayed to the player
def quiz_questions_and_answers(quiz): # Function to display the questions and answer options to the player
    import random
    score = 0
    for question in quiz: # Loop to display the specified number of questions and answer options to the player
        print(f"\nQuestion: {question['question']}")

        # The order of answer options displayed is randomised
        shuffled_options = question['options'].copy()
        random.shuffle(shuffled_options)

        for i, option in enumerate(shuffled_options, start=1): # Each answer option is shown with a unique selectable number
            print(f"{i}. {option}")

        answer = input("Your answer: ")
        if not answer: # Triggers if the player doesn't enter anything'
            print("You haven't answered yet... Please enter your answer.")
        elif answer.isdigit() and 1 <= int(answer) <= len(shuffled_options): # Triggers if the player enters a number within the range of the answer options
            if shuffled_options[int(answer) - 1] == question['correct_answer']:# Triggers if the player's answer is correct'
                print("Correct!")
                score += 1
            else: # Triggers if the player's answer is incorrect
                print(f"Wrong! The correct answer is {question['correct_answer']}.")
        else: # Triggers if the player enters a number outside the range of the answer options
            print("That answer does not correspond to any of the stated options. Please enter a number between 1 and " + str(len(shuffled_options)) + "")
    return score





def score_storage (name, category, score, number_of_questions):
    with open("scores.txt", "a") as f:
        f.write("Name: " + str(name) + ". Selected category: " + str(category) +  ". Selected questions score: " + str(score) + " " + ". Overall score: " + str(score/number_of_questions*100) + "% \n")
    print("Your score has been saved.")



def play_quiz():
    # A quick introduction of what is Quizarium
    print("Hello there, and welcome to the Quizarium! A quiz where you can demonstrate your knowledge in your preferred topic.")

    # Calls the function to get the name of the player
    player_name = get_name()

    # Calls the function using as a parameter the keys of the dictionary
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

    score_storage(player_name, player_chosen_category, player_score, player_number_of_questions)




def yes_no_answer(question):
    while True:
        answer = input(question)
        if answer == "Y" or answer == "y":
            return True
        elif answer == "N" or answer == "n":
            return False
        else:
            print("Please enter Y or N. ")

keep_playing = True

while keep_playing:
    play_quiz()
    continue_playing = yes_no_answer("Would you like to play another quiz? (Please enter Y for Yes and N for No) ")
    if not continue_playing:
        continue_playing_2 = yes_no_answer("Does anybody else want to play? (Please enter Y for Yes and N for No) ")
        if not continue_playing_2:
            keep_playing = False
            print("Thank you for playing Quizarium! See you soon!")
        else:
            continue
    else:
        continue






