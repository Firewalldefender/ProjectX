from question_collection import QuestionCollection
from player import Player
from enemy import Enemy


class Combat:
    def __init__(
        self, player: Player, enemy: Enemy, question_collection: QuestionCollection
    ):
        self.player = player
        self.enemy = enemy
        self.question_collection = question_collection

    def run_combat(self):
        print("--Combat started--")
        combat_over = False
        while not combat_over:
            question = self.question_collection.get_question(self.enemy.difficulty)
            question.display()
            player_answer = input("Answer: ").upper()
            labels = {"A": 0, "B": 1, "C": 2, "D": 3}
            if labels[player_answer] == question.answer:
                self.enemy.take_damage(self.enemy.attack)
            else:
                self.player.take_damage(self.enemy.attack)
            if not self.player.is_alive():
                print("YOU DIED")
                pass
            if not self.enemy.is_alive():
                combat_over = True
        print(f"You deafeated the {self.enemy.name}")
