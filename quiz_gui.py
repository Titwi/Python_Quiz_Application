import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLabel, QLineEdit,
                             QRadioButton, QButtonGroup, QMessageBox, QComboBox,
                             QSpinBox, QTextEdit, QScrollArea)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from databases.quiz_database import quiz_questions


class QuizApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player_name = ""
        self.selected_category = ""
        self.num_questions = 0
        self.quiz_questions_list = []
        self.current_question_index = 0
        self.score = 0

        self.setWindowTitle("Quizarium")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: blue;")

        self.show_welcome_screen()

    def show_welcome_screen(self):
        """Display the welcome screen with name input"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Title
        title = QLabel("Welcome to Quizarium!")
        title.setFont(QFont("Arial", 24, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Subtitle
        subtitle = QLabel("A quiz where you can demonstrate your knowledge\nin your preferred topic.")
        subtitle.setFont(QFont("Arial", 14))
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)

        # Name input
        name_label = QLabel("What is your name?")
        name_label.setFont(QFont("Arial", 12))
        name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(name_label)

        self.name_input = QLineEdit()
        self.name_input.setMaximumWidth(300)
        self.name_input.setFont(QFont("Arial", 12))
        layout.addWidget(self.name_input, alignment=Qt.AlignCenter)

        # Start button
        start_button = QPushButton("Start Quiz")
        start_button.setFont(QFont("Arial", 12))
        start_button.setMaximumWidth(200)
        start_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        start_button.clicked.connect(self.validate_name)
        layout.addWidget(start_button, alignment=Qt.AlignCenter)

        central_widget.setLayout(layout)

    def validate_name(self):
        """Validate the player's name"""
        name = self.name_input.text().strip()

        if not name:
            QMessageBox.warning(self, "Error", "You haven't answered yet...")
            return

        if not all(ch.isalpha() or ch in " -'" for ch in name):
            QMessageBox.warning(self, "Error",
                                "Please enter your name using letters only\n(no numbers or symbols).")
            return

        self.player_name = name
        self.show_category_selection()

    def show_category_selection(self):
        """Display the category selection screen"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Greeting
        greeting = QLabel(f"Nice to meet you, {self.player_name}!")
        greeting.setFont(QFont("Arial", 18, QFont.Bold))
        greeting.setAlignment(Qt.AlignCenter)
        layout.addWidget(greeting)

        # Instructions
        instructions = QLabel("Please select a category:")
        instructions.setFont(QFont("Arial", 14))
        instructions.setAlignment(Qt.AlignCenter)
        layout.addWidget(instructions)

        # Category dropdown
        self.category_combo = QComboBox()
        self.category_combo.setFont(QFont("Arial", 12))
        self.category_combo.setMaximumWidth(400)
        self.category_combo.addItems(list(quiz_questions.keys()))
        layout.addWidget(self.category_combo, alignment=Qt.AlignCenter)

        # Continue button
        continue_button = QPushButton("Continue")
        continue_button.setFont(QFont("Arial", 12))
        continue_button.setMaximumWidth(200)
        continue_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
        """)
        continue_button.clicked.connect(self.select_category)
        layout.addWidget(continue_button, alignment=Qt.AlignCenter)

        central_widget.setLayout(layout)

    def select_category(self):
        """Store selected category and move to question count selection"""
        self.selected_category = self.category_combo.currentText()
        self.show_question_count_selection()

    def show_question_count_selection(self):
        """Display the question count selection screen"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Category info
        category_label = QLabel(f"Category: {self.selected_category}")
        category_label.setFont(QFont("Arial", 16, QFont.Bold))
        category_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(category_label)

        # Instructions
        total_available = len(quiz_questions[self.selected_category])
        instructions = QLabel(f"There are {total_available} questions available.\nHow many would you like to answer?")
        instructions.setFont(QFont("Arial", 14))
        instructions.setAlignment(Qt.AlignCenter)
        layout.addWidget(instructions)

        # Spin box for question count
        self.question_count_spin = QSpinBox()
        self.question_count_spin.setFont(QFont("Arial", 12))
        self.question_count_spin.setMinimum(1)
        self.question_count_spin.setMaximum(total_available)
        self.question_count_spin.setValue(min(10, total_available))
        self.question_count_spin.setMaximumWidth(100)
        layout.addWidget(self.question_count_spin, alignment=Qt.AlignCenter)

        # Start quiz button
        start_button = QPushButton("Start Quiz")
        start_button.setFont(QFont("Arial", 12))
        start_button.setMaximumWidth(200)
        start_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        start_button.clicked.connect(self.start_quiz)
        layout.addWidget(start_button, alignment=Qt.AlignCenter)

        central_widget.setLayout(layout)

    def start_quiz(self):
        """Initialize quiz with selected parameters"""
        self.num_questions = self.question_count_spin.value()
        all_questions = quiz_questions[self.selected_category]
        self.quiz_questions_list = random.sample(all_questions, self.num_questions)
        self.current_question_index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        """Display the current question"""
        if self.current_question_index >= len(self.quiz_questions_list):
            self.show_results()
            return

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Progress indicator
        progress = QLabel(f"Question {self.current_question_index + 1} of {self.num_questions}")
        progress.setFont(QFont("Arial", 12))
        progress.setAlignment(Qt.AlignCenter)
        layout.addWidget(progress)

        # Score display
        score_label = QLabel(f"Current Score: {self.score}")
        score_label.setFont(QFont("Arial", 12))
        score_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(score_label)

        # Question text
        current_q = self.quiz_questions_list[self.current_question_index]
        question_label = QLabel(current_q['question'])
        question_label.setFont(QFont("Arial", 14, QFont.Bold))
        question_label.setWordWrap(True)
        question_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(question_label)

        # Answer options
        self.answer_group = QButtonGroup()
        shuffled_options = current_q['options'].copy()
        random.shuffle(shuffled_options)

        for i, option in enumerate(shuffled_options):
            radio = QRadioButton(option)
            radio.setFont(QFont("Arial", 12))
            self.answer_group.addButton(radio, i)
            layout.addWidget(radio)

        self.shuffled_options = shuffled_options

        # Submit button
        submit_button = QPushButton("Submit Answer")
        submit_button.setFont(QFont("Arial", 12))
        submit_button.setMaximumWidth(200)
        submit_button.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #e68900;
            }
        """)
        submit_button.clicked.connect(self.check_answer)
        layout.addWidget(submit_button, alignment=Qt.AlignCenter)

        central_widget.setLayout(layout)

    def check_answer(self):
        """Check if the selected answer is correct"""
        selected_button = self.answer_group.checkedButton()

        if not selected_button:
            QMessageBox.warning(self, "Error", "Please select an answer!")
            return

        current_q = self.quiz_questions_list[self.current_question_index]
        selected_index = self.answer_group.id(selected_button)
        selected_answer = self.shuffled_options[selected_index]

        if selected_answer == current_q['correct_answer']:
            QMessageBox.information(self, "Correct!", "That's the right answer!")
            self.score += 1
        else:
            QMessageBox.information(self, "Wrong",
                                    f"Sorry, the correct answer is:\n{current_q['correct_answer']}")

        self.current_question_index += 1
        self.show_question()

    def show_results(self):
        """Display the final results"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Results title
        title = QLabel("Quiz Complete!")
        title.setFont(QFont("Arial", 24, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Score display
        percentage = (self.score / self.num_questions) * 100
        score_label = QLabel(f"{self.player_name}, your final score is:\n{self.score} out of {self.num_questions}")
        score_label.setFont(QFont("Arial", 16))
        score_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(score_label)

        percentage_label = QLabel(f"Overall score: {percentage:.1f}%")
        percentage_label.setFont(QFont("Arial", 16, QFont.Bold))
        percentage_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(percentage_label)

        # Save score button
        save_button = QPushButton("Save Score")
        save_button.setFont(QFont("Arial", 12))
        save_button.setMaximumWidth(200)
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        save_button.clicked.connect(self.save_score)
        layout.addWidget(save_button, alignment=Qt.AlignCenter)

        # View scores button
        view_button = QPushButton("View High Scores")
        view_button.setFont(QFont("Arial", 12))
        view_button.setMaximumWidth(200)
        view_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
        """)
        view_button.clicked.connect(self.view_scores)
        layout.addWidget(view_button, alignment=Qt.AlignCenter)

        # Play again button
        restart_button = QPushButton("Play Again")
        restart_button.setFont(QFont("Arial", 12))
        restart_button.setMaximumWidth(200)
        restart_button.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #e68900;
            }
        """)
        restart_button.clicked.connect(self.restart_quiz)
        layout.addWidget(restart_button, alignment=Qt.AlignCenter)

        # Exit button
        exit_button = QPushButton("Exit")
        exit_button.setFont(QFont("Arial", 12))
        exit_button.setMaximumWidth(200)
        exit_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
        """)
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button, alignment=Qt.AlignCenter)

        central_widget.setLayout(layout)

    def save_score(self):
        """Save the score to scores.txt"""
        percentage = (self.score / self.num_questions) * 100
        try:
            with open("scores.txt", "a") as f:
                f.write(
                    f"Name: {self.player_name}, Selected questions score: {self.score}/{self.num_questions}, Overall score: {percentage:.1f}%\n")
            QMessageBox.information(self, "Success", "Your score has been saved!\nThank you for playing Quizarium!")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Could not save score: {str(e)}")

    def view_scores(self):
        """Display saved scores"""
        try:
            with open("scores.txt", "r") as f:
                scores_content = f.read()

            if not scores_content:
                QMessageBox.information(self, "High Scores", "No scores saved yet!")
                return

            # Create a new window to display scores
            scores_dialog = QMessageBox(self)
            scores_dialog.setWindowTitle("High Scores")
            scores_dialog.setText("Saved Scores:")
            scores_dialog.setDetailedText(scores_content)
            scores_dialog.exec_()
        except FileNotFoundError:
            QMessageBox.information(self, "High Scores", "No scores saved yet!")

    def restart_quiz(self):
        """Restart the quiz"""
        reply = QMessageBox.question(self, "Restart",
                                     "Do you want to play again with a different player?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.show_welcome_screen()
        else:
            self.show_category_selection()


def main():
    app = QApplication(sys.argv)
    window = QuizApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()