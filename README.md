# CLI Quiz Application

A lightweight command-line quiz application written in Python 3 using only the standard library. The app loads multiple-choice questions from an external JSON file, accepts user input, provides immediate feedback, calculates scores, and displays a summary review at the end.

---

## Approach

The project is structured around clean procedural programming and separation of concerns:
- **Data storage**: Question definitions (prompts, options, and answers) are stored separately in `questions.json`.
- **Application flow**: Handled by small functions in `quiz.py`:
  - `load_questions()`: Safely reads and validates the JSON file.
  - `get_valid_answer()`: Continuously prompts the user until a valid option (A, B, C, or D) is provided.
  - `ask_question()`: Presents the question, evaluates the answer, and gives immediate feedback.
  - `calculate_result()`: Computes the percentage and assigns a performance remark.
  - `show_summary()`: Displays the final score breakdown and missed questions.
  - `main()`: Orchestrates the overall quiz loop, question count selection, and replay options.

---

## Features

- **JSON-backed question bank**: Questions and options are loaded from `questions.json`.
- **Randomized questions**: Questions are shuffled every time the quiz runs (`random.shuffle`).
- **Configurable question count**: Users can choose how many questions to attempt or press Enter to answer all available questions.
- **Immediate feedback**: Tells the user immediately whether they were right or wrong, revealing the correct answer on mistakes.
- **Input validation**: Gracefully handles invalid choices (like lowercase letters, numbers, or empty inputs) without crashing or skipping the question.
- **Detailed summary**: Displays total questions, correct count, wrong count, final score, percentage, and a remark (e.g., "Excellent!", "Good effort!", "Needs practice.").
- **Missed question review**: Lists all questions answered incorrectly alongside the user's answer and the correct answer.
- **Play again loop**: Prompts the user to restart the quiz or exit cleanly.
- **Error handling**: Catches missing or corrupted JSON files, empty question lists, and keyboard interrupts (`Ctrl+C` / EOF).

---

## Project Structure

```text
cli_quiz_app/
│
├── quiz.py            # Main application script
├── questions.json     # Question bank (12 Python basics questions)
├── sample_output.txt  # Real terminal output from a live test run
└── README.md          # Project documentation and interview answers
```

---

## How to Run

1. Open a terminal or VS Code in the project folder:
   ```bash
   cd cli_quiz_app
   ```
2. Run the application using Python 3:
   ```bash
   python quiz.py
   ```

---

## `questions.json` Format

The question bank is a JSON array of objects. Each object contains:
- `question`: The text of the question.
- `options`: A dictionary mapping option letters (`A`, `B`, `C`, `D`) to their respective text.
- `answer`: The letter corresponding to the correct option.

Example:
```json
[
  {
    "question": "Which keyword is used to define a function in Python?",
    "options": {
      "A": "function",
      "B": "def",
      "C": "fun",
      "D": "define"
    },
    "answer": "B"
  }
]
```

---

## Outcome

Running the application allows users to test their Python basics interactively directly from the command line. A real run transcript capturing invalid input handling, wrong answer handling, final summary calculation, and review of missed questions is recorded in `sample_output.txt`.

---

## Interview Questions & Answers

### 1. How should quiz questions be stored?
In Python applications, questions are best stored using a **list of dictionaries**. 
- Each dictionary represents a single question with keys for the question text (`"question"`), the available choices (`"options"` as a dictionary or list), and the right answer (`"answer"`).
- For persistence and ease of editing, storing them externally in a **JSON file** (`questions.json`) is the standard practice. Python's built-in `json.load()` converts the JSON structure directly into Python lists and dictionaries with a single line of code.

### 2. Why separate data from program logic?
- **Maintainability & Extensibility**: You can add, edit, or delete questions without touching a single line of Python code. Non-programmers (such as teachers or content writers) can update questions without the risk of breaking program logic.
- **Reusability**: The exact same `quiz.py` engine can be used for any quiz topic (e.g., JavaScript, History, Math) simply by pointing to a different JSON file.
- **Bug Prevention**: Modifying code to update data introduces risks of syntax errors or unintended logic bugs. Isolating data into JSON keeps the codebase clean and safe.

### 3. How do you randomly select questions in Python?
Python's standard `random` module provides two common approaches:
- **`random.shuffle(list)`**: Shuffles an existing list in-place. If you want to allow the user to select $N$ questions, you shuffle the full list and slice the first $N$ items: `selected = questions[:n]`. This ensures every question in the set is unique and randomly ordered.
- **`random.sample(population, k)`**: Returns a new list of $k$ unique elements chosen randomly from the population without modifying the original list.

For this quiz application, `random.shuffle()` followed by slicing was chosen because it allows the question order to be thoroughly randomized every round, while easily supporting custom question counts.
