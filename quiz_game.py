"""Quiz Game - Test your knowledge"""
import random

QUESTIONS = [
    {"q": "What is the capital of France?", "a": "paris"},
    {"q": "What planet is known as the Red Planet?", "a": "mars"},
    {"q": "What is 7 x 8?", "a": "56"},
    {"q": "What language is this game written in?", "a": "python"},
    {"q": "How many continents are there?", "a": "7"},
    {"q": "What is the largest ocean?", "a": "pacific"},
    {"q": "What year did World War II end?", "a": "1945"},
    {"q": "What is H2O commonly known as?", "a": "water"},
]

def play():
    questions = random.sample(QUESTIONS, min(5, len(QUESTIONS)))
    score = 0

    print("Welcome to the Quiz Game!")
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
