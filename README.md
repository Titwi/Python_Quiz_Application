# Quizarium

A quiz application where you can demonstrate your knowledge in your preferred topic.

## Features

- **Two Interfaces**: Choose between a command-line interface or a graphical user interface (GUI)
- **Multiple Categories**: Test your knowledge in:
  - General Knowledge
  - History & Geography
  - Modern Music & Literature
  - Games & Riddles
- **Customizable Quiz Length**: Choose how many questions you want to answer
- **Score Tracking**: Save your scores and view high scores
- **Randomized Questions**: Questions and answer options are shuffled for variety

## Installation

### Requirements

- Python 3.x
- PyQt5 (for GUI version only)

### Install Dependencies

```bash
pip install PyQt5
```

## Usage

### GUI Version

Run the graphical interface:

```bash
python quiz_gui.py
```

Features:
- Welcome screen with name input
- Category selection dropdown
- Question count selector
- Visual feedback for correct/incorrect answers
- Score saving and viewing

### Command-Line Version

Run the text-based interface:

```bash
python user_interface.py
```

Features:
- Interactive text prompts
- Play multiple quizzes in one session
- Multiple player support
- Score tracking to `scores.txt`

## Project Structure

```
.
├── quiz_gui.py              # GUI application using PyQt5
├── user_interface.py        # Command-line interface
├── databases/
│   └── quiz_database.py     # Question database
└── scores.txt               # Saved scores (created on first save)
```

## How to Play

1. **Enter Your Name**: Start by providing your name
2. **Choose a Category**: Select from the available quiz categories
3. **Select Question Count**: Decide how many questions you want to answer
4. **Answer Questions**: Multiple-choice questions with randomized options
5. **View Your Score**: See your final score and percentage
6. **Save Your Score**: Optionally save your score to track progress
7. **Play Again**: Start a new quiz or exit

## Score Format

Scores are saved in the following format:
```
Name: [Player Name], Selected questions score: [Score]/[Total], Overall score: [Percentage]%
```

## License

This project is open source and available for educational purposes.
