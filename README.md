# Quizarium

A command-line quiz application where you can demonstrate your knowledge in your preferred topic.

## Features

- **Multiple Categories**: Test your knowledge in:
  - General Knowledge (33 questions)
  - History & Geography (30 questions)
  - Modern Music & Literature (25 questions)
  - Games & Riddles (25 questions)
- **Customizable Quiz Length**: Choose how many questions you want to answer from the available pool
- **Persistent Score Database**: All scores are automatically saved and retained across sessions using JSON storage
- **Comprehensive Score Tracking**: View top 3 scores, average scores, and complete player rankings per category
- **Randomised Questions**: Questions and answer options are shuffled for variety
- **Multi-Player Support**: Multiple players can play in one session
- **Returning Player Feature**: Continue playing without re-entering your name

## Installation

### Requirements

- Python 3.x

### No Additional Dependencies Required

The application uses only Python standard libraries (json, random).

## Usage

Run the application:

```bash
python user_interface.py
```

### Features

- Interactive text prompts
- Play multiple quizzes in one session
- Multiple player support
- Automatic score persistence across sessions
- Returning players skip name entry and go directly to category selection
- Instant feedback on correct/incorrect answers
- Top 3 scores displayed after each quiz

## Project Structure

```
.
├── user_interface.py        # Main quiz application
├── databases/
│   └── quiz_database.py     # Question database with 113+ questions
├── quiz_scores.json         # Persistent score database (created automatically)
└── quiz_scores.txt          # Human-readable score report (generated at session end)
```

## How to Play

1. **Enter Your Name** (first-time players only): Provide your username
2. **Choose a Category**: Select from 4 available quiz categories by entering the corresponding number
3. **Select Question Count**: Choose how many questions you want to answer (1 to total available in category)
4. **Answer Questions**: Multiple-choice questions with randomised options - enter the number of your answer
5. **View Your Score**: See your final score, total questions, and percentage (automatically saved to database)
6. **View Top 3 Scores**: Automatically see the top 3 scores for your chosen category
7. **Play Again**:
   - Answer "Y" to play another quiz (you'll go directly to category selection)
   - Answer "N" if you're done, then choose if another player wants to join
8. **Session End Report**: When all players are done, view:
   - Top 3 scores per category
   - Average score across all players in each category
   - Complete score summary automatically saved to `quiz_scores.txt`

## Score Tracking System

### Automatic Saves
- Scores are automatically saved to `quiz_scores.json` after each quiz completion
- All scores persist across different sessions
- The database grows with every player and quiz attempt
- Previous scores are loaded automatically when the application starts

### Score Report Format (quiz_scores.txt)

For each category, the report shows:

1. **Top 3 Player Scores**: Best performers ranked by percentage
2. **Average Score**: Mean percentage across all players in that category
3. **All Player Scores**: Complete ranking of all attempts

Example:
```
================================================================================
CATEGORY: General Knowledge
================================================================================

TOP 3 PLAYER SCORES:
--------------------------------------------------------------------------------
Rank   Name                 Score           Percentage
--------------------------------------------------------------------------------
1      Alice                10/10           100.00%
2      Bob                  8/10            80.00%
3      Charlie              7/10            70.00%

AVERAGE SCORE:
--------------------------------------------------------------------------------
Average across all players: 83.33%

ALL PLAYER SCORES:
--------------------------------------------------------------------------------
Rank   Name                 Score           Percentage
--------------------------------------------------------------------------------
1      Alice                10/10           100.00%
2      Bob                  8/10            80.00%
3      Charlie              7/10            70.00%
```

## Question Database

The quiz contains 113 questions across 4 categories:
- **General Knowledge**: 33 questions covering science, culture, history, geography, and more
- **History & Geography**: 30 questions about world history, ancient civilizations, and geography
- **Modern Music & Literature**: 25 questions about music artists, bands, books, and authors
- **Games & Riddles**: 25 questions about board games, video games, nursery rhymes, and brain teasers

## References
Quiz questions were sourced from the following website:

Cacic, M. (2025). 100 General Trivia Questions |Top Quiz Questions – Opinion Stage. [online] Available at: https://www.opinionstage.com/blog/trivia-questions/ [Accessed 07 Nov 2025]

## License

This project is open source and available for educational purposes.
