import json
import random
from question import Question


class QuestionCollection:
    def __init__(self):
        self.questions = self.load_questions()
        self.used_questions = {}

    def load_questions(self):
        with open("questions.json", "r") as file:
            data = json.load(file)
        questions = []
        for q in data["questions"]:
            q = Question(
                id=q["id"],
                difficulty=q["difficulty"],
                question=q["question"],
                options=q["options"],
                answer=q["answer"],
            )
            questions.append(q)
        return questions

    def get_question(self, difficulty):
        filtered_questions = [
            q
            for q in self.get_questions
            if q.id not in self.used_questions and q.difficulty == difficulty
        ]
        return random.choice(filtered_questions)

    def mark_used(self, id):
        self.used_questions.add(id)
