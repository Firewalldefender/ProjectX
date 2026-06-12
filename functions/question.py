from rich import print

class Question:
    def __init__(self, id, difficulty, question, options, answer):
        self.id = id
        self.difficulty = difficulty
        self.question = question
        self.options = options
        self.answer = answer

    def display(self):
        print(self.question)
        labels = ["A", "B", "C", "D"]
        for i, q in enumerate(self.options):
            print(f"{labels[i]} {q}", end="\t")
