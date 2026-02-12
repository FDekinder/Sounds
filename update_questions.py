"""Daily quiz question updater - Uses Anthropic AI to generate 5 new questions and commits to git."""
import json
import os
import subprocess
import sys
from datetime import date

try:
    import anthropic
except ImportError:
    print("Error: 'anthropic' package not installed.")
    print("Run: pip install anthropic")
    sys.exit(1)

QUESTIONS_FILE = os.path.join(os.path.dirname(__file__), "daily_questions.json")

PROMPT = """Generate exactly 5 trivia quiz questions. Mix categories: science, history, geography, math, pop culture, nature, sports, etc.

Rules:
- Each answer must be short (1-3 words, all lowercase)
- Questions should be fun and not too hard
- Do NOT repeat common questions like "capital of France" or "Red Planet"
- Be creative and varied

Respond with ONLY valid JSON, no other text. Format:
[
  {"q": "question text here?", "a": "answer"},
  {"q": "question text here?", "a": "answer"},
  {"q": "question text here?", "a": "answer"},
  {"q": "question text here?", "a": "answer"},
  {"q": "question text here?", "a": "answer"}
]"""


def generate_questions():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("Set it with: set ANTHROPIC_API_KEY=your-key-here")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    print(f"Generating new questions for {date.today()}...")
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=512,
        messages=[{"role": "user", "content": PROMPT}],
    )

    response_text = message.content[0].text.strip()

    try:
        questions = json.loads(response_text)
    except json.JSONDecodeError:
        print("Error: AI response was not valid JSON.")
        print(f"Response: {response_text}")
        sys.exit(1)

    if not isinstance(questions, list) or len(questions) != 5:
        print(f"Error: Expected 5 questions, got {len(questions) if isinstance(questions, list) else 'invalid data'}.")
        sys.exit(1)

    for q in questions:
        if "q" not in q or "a" not in q:
            print(f"Error: Invalid question format: {q}")
            sys.exit(1)
        q["a"] = q["a"].lower().strip()

    data = {
        "date": str(date.today()),
        "questions": questions,
    }

    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Saved 5 new questions to {QUESTIONS_FILE}")
    for i, q in enumerate(questions, 1):
        print(f"  {i}. {q['q']} -> {q['a']}")

    return True


def git_commit_and_push():
    """Stage the updated questions file, commit, and push to git."""
    repo_dir = os.path.dirname(__file__)

    try:
        subprocess.run(["git", "add", "daily_questions.json"], cwd=repo_dir, check=True)
        commit_msg = f"Update daily quiz questions for {date.today()}"
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=repo_dir, check=True)
        subprocess.run(["git", "push"], cwd=repo_dir, check=True)
        print(f"\nCommitted and pushed: {commit_msg}")
    except subprocess.CalledProcessError as e:
        print(f"\nGit error: {e}")
        print("Questions were saved locally but git commit/push failed.")


if __name__ == "__main__":
    if generate_questions():
        git_commit_and_push()
