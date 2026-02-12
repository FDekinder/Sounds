"""Quiz Game - Test your knowledge with daily AI-generated questions"""
import json
import os
from datetime import date

QUESTIONS_FILE = os.path.join(os.path.dirname(__file__), "daily_questions.json")

FALLBACK_QUESTIONS = [
    {"q": "What is the capital of France?", "a": "paris"},
    {"q": "What planet is known as the Red Planet?", "a": "mars"},
    {"q": "What is 7 x 8?", "a": "56"},
    {"q": "How many continents are there?", "a": "7"},
    {"q": "What is the largest ocean?", "a": "pacific"},
]


def load_daily_questions():
    """Load AI-generated questions from JSON, or fall back to defaults."""
    today = str(date.today())

    if os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if data.get("date") == today:
            print("[AI-generated questions for today]\n")
            return data["questions"]
        else:
            print("[Questions are outdated - run update_questions.py to refresh]\n")

    print("[Using fallback questions - run update_questions.py for AI questions]\n")
    return FALLBACK_QUESTIONS

def play():
    questions = load_daily_questions()
    score = 0

    print("Welcome to the Quiz Game!")
    print(f"Today's date: {date.today()}")
    print(f"Answer {len(questions)} questions.\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['q']}")
        answer = input("Your answer: ").lower().strip()

        if answer == q["a"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The answer was: {q['a']}\n")

    print(f"Final Score: {score}/{len(questions)}")

    if score == len(questions):
        print("Perfect score!")
    elif score >= len(questions) // 2:
        print("Good job!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    play()
