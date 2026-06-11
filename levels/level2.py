from levels.base_level import Level


class Level2(Level):
    def __init__(self):
        super().__init__(name="level2")

        self.choices = [
            {
                "text": "Level2 Placeholder",
                "next": "victory",
                "combat": True,
                "enemies": ["SlitheringSnake"],
                "message": "You venture on",
            }
        ]

    def display(self):
        print(
            "You wake up in a deep dark cell under the palace of King  Python. He threw you in the dungeon because you mocked the Python language. Your mission is to escape, but beware dangers await you everywhere !"
        )
