from levels.base_level import Level
from rich import print

# The Coldblooded Hatchery


class Level2(Level):
    def __init__(self):
        super().__init__(name="level2")

        self.choices = [
            {
                "text": "Hide from it", 
                "next": "level3",
                "combat": True,
                "enemies": [
                    {"name": "SlitheringSnake", "waves": 1},
                    {"name": "WarriorWorm", "waves": 1},
                    {"name": "SlitheringSnake", "waves": 1}
                ],
                "message": "You hid from the PythonsPartisan, but smaller snakes appeared. You killed them succesfully!",
            },
            {
                "text": "Fight it",
                "next": "level3",
                "combat": True,
                "enemies": [{"name": "PythonsPartisan", "waves": 1}],
                "message": "You took the chance and killed the PythonsPartisan.",
            }
        ]

    def display(self):
        print(
            "You finally made it out of the dark cell. You look around in a dim light and cold environment. As you go forward, you notice eggshells. Welcome in the 'The Coldblooded Hatchery'. By mistake, you step on an egg and a big snake appears."
        )
