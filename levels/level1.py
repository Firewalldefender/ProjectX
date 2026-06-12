from levels.base_level import Level
from rich import print

# Deepest Dungeon Stall


class Intro(Level):
    def __init__(self):
        super().__init__(name="Intro")

        self.choices = [
            {
                "text": "Leave the cell",
                "next": "level2",
                "combat": True,
                "enemies": [{"name": "SlitheringSnake", "waves": 1}],
                "message": "You step out of the cell",
            }
        ]

    def display(self):
        print(
            "[red]You wake up in a deep dark cell under the palace of King  Python. He threw you in the dungeon because you mocked the Python language. Your mission is to escape, but beware dangers await you everywhere !"
        )
