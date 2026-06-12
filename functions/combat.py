from functions.question_collection import QuestionCollection
from functions.player import Player
from functions.enemy import Enemy
from rich import print

class Combat:
    def __init__(
        self,
        player: Player,
        enemies: list[Enemy],
        question_collection: QuestionCollection,
    ):
        self.player = player
        self.enemies = enemies
        self.question_collection = question_collection

    def run_combat(self):
        print("--- Combat started ---")
        for enemy in self.enemies:
            print(f"--- {enemy.max_waves} {enemy.name} ---")
            while enemy.is_active():
                question = self.question_collection.get_question(enemy.difficulty)
                self.question_collection.mark_used(question.id)
                question.display()
                player_answer = input("Answer: ").upper()
                labels = {"A": 0, "B": 1, "C": 2, "D": 3}
                if labels.get(player_answer) == question.answer:
                    enemy.take_damage(enemy.attack)
                    print(f"You dealt {enemy.attack} damage to {enemy.name}!")
                else:
                    self.player.take_damage(enemy.attack)
                    print(f"{enemy.name} dealt {enemy.attack} damage to you!")

                print(f"Your HP: {self.player.health}/{self.player.max_health}")
                print(
                    f"{enemy.name} HP: {enemy.health}/{enemy.max_health}"
                )

                if not self.player.is_alive():
                    print(f"You were defeated by {enemy.name}!")
                    return False

                if enemy.is_defeated():
                    print(f"{enemy.name} has been defeated!")
            enemy.reset()   

        print("You defeated all enemies!")
        print("--- Combat ended ---")
        return True
