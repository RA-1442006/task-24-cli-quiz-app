import json
import random
import os

# load questions from json file
def load_questions(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            if not isinstance(data, list) or len(data) == 0:
                print("Error: The question file is empty or formatted incorrectly.")
                return None
            return data
    except FileNotFoundError:
        print(f"Error: Could not find '{filename}'. Make sure the file exists.")
        return None
    except json.JSONDecodeError:
        print(f"Error: '{filename}' contains invalid JSON.")
        return None

# keep asking until user enters A, B, C, or D
def get_valid_answer():
    while True:
        choice = input("Your answer (A/B/C/D): ").strip().upper()
        if choice in ["A", "B", "C", "D"]:
            return choice
        print("Invalid input! Please enter A, B, C, or D.")

# display question, get answer, and check correctness
def ask_question(q, q_num):
    print(f"\nQuestion {q_num}: {q['question']}")
    for letter in ["A", "B", "C", "D"]:
        print(f"  {letter}) {q['options'][letter]}")

    user_answer = get_valid_answer()
    correct_answer = q["answer"]

    if user_answer == correct_answer:
        print("Correct!")
        return True, user_answer
    else:
        correct_text = q["options"][correct_answer]
        print(f"Wrong! The correct answer was {correct_answer}) {correct_text}")
        return False, user_answer

# calculate percentage and decide remark
def calculate_result(score, total):
    if total == 0:
        return 0.0, "No questions attempted."
    percentage = round((score / total) * 100, 1)
    if percentage >= 80:
        remark = "Excellent!"
    elif percentage >= 50:
        remark = "Good effort!"
    else:
        remark = "Needs practice."
    return percentage, remark

# print final quiz results and review missed questions
def show_summary(total, correct, wrong_list):
    wrong = total - correct
    percentage, remark = calculate_result(correct, total)

    print("\n--- Quiz Results ---")
    print(f"Total Questions : {total}")
    print(f"Correct Answers : {correct}")
    print(f"Wrong Answers   : {wrong}")
    print(f"Final Score     : {correct}/{total}")
    print(f"Percentage      : {percentage}%")
    print(f"Remark          : {remark}")

    if wrong_list:
        print("\nQuestions you missed:")
        for item in wrong_list:
            print(f"- Question: {item['question']}")
            print(f"  Your answer:    {item['user_answer']}")
            print(f"  Correct answer: {item['correct_answer']}) {item['correct_text']}")
    else:
        print("\nAwesome job! You got every question right!")

def main():
    # locate questions.json in the same folder as quiz.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "questions.json")

    while True:
        questions = load_questions(file_path)
        if not questions:
            print("Cannot start quiz without questions. Exiting.")
            return

        # randomize question order each run
        random.shuffle(questions)

        total_available = len(questions)
        print("\n=== Welcome to the Python Basics Quiz ===")
        print(f"Total questions available: {total_available}")

        # let user choose question count
        while True:
            user_input = input(f"How many questions would you like to attempt? (1-{total_available}, press Enter for all): ").strip()
            if user_input == "":
                num_questions = total_available
                break
            elif user_input.isdigit() and 1 <= int(user_input) <= total_available:
                num_questions = int(user_input)
                break
            else:
                print(f"Please enter a valid number between 1 and {total_available}.")

        selected_questions = questions[:num_questions]
        score = 0
        wrong_list = []

        # ask each question
        for index, q in enumerate(selected_questions, start=1):
            is_correct, user_answer = ask_question(q, index)
            if is_correct:
                score += 1
            else:
                wrong_list.append({
                    "question": q["question"],
                    "user_answer": user_answer,
                    "correct_answer": q["answer"],
                    "correct_text": q["options"][q["answer"]]
                })

        # show summary at end
        show_summary(num_questions, score, wrong_list)

        # ask to play again
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != "y":
            print("\nThanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nQuiz exited. Goodbye!")
