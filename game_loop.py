from functions.combat import Combat
from functions.enemy import Enemy
from functions.player import Player
from functions.question_collection import QuestionCollection
from levels.base_level import Level
from levels.level1 import Intro
from levels.level2 import Level2
from levels.level3 import Level3


class Game:
    def __init__(self):
        self.player = Player(name="Player")
        self.question_collection = QuestionCollection()
        self.levels = {}
        self.enemies = {}
        self.current_level = "Intro"
        self.load_levels()
        self.load_enemies()

    def load_levels(self):
        level_list = [Intro(), Level2(),Level3()]
        for level in level_list:
            self.levels[level.name] = level

    def load_enemies(self):
        enemie_list = [
            Enemy("SlitheringSnake", 20, "easy"),
            Enemy("PythonsPartisan", 40, "medium"),
        ]
        for enemy in enemie_list:
            self.enemies[enemy.name] = enemy

    def start(self):
        # TODO input validation
        player_name = input("What is your name?: ")
        self.player.name = player_name
        while self.current_level not in ("victory", "defeat"):
            self.run_level(self.current_level)
        if self.current_level == "victory":
            print("YOU WIN")
        else:
            print("YOU DIED")
            # TODO restart

    def run_level(self, level: Level):
        level = self.levels[level]
        level.display()
        for i, c in enumerate(level.choices):
            print(f"{i + 1} {c['text']}", end="\t")
        # TODO input validation
        print()
        player_choice = int(input("Your choice: ")) - 1
        choice = level.choices[player_choice]

        if choice["combat"]:
            # TODO handle multiple enemies
            combat_loop = Combat(
                self.player,
                self.enemies[choice["enemies"][0]],
                self.question_collection,
            )
            player_won = combat_loop.run_combat()
            if not player_won:
                self.current_level = "defeat"

        self.current_level = choice["next"]
        print(choice["message"])
