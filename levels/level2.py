from levels.base_level import Level

# The Coldblooded Hatchery


class Level2(Level):
    def __init__(self):
        super().__init__(name="level2")

        self.choices = [
            {
                "text": "Hide from it", 
                "next": "level3",
                "combat": True,
                "enemies": ["SlitheringSnake"],
                "message": "You venture on",
            },
            {
                "text": "Fight it",
                "next": "level3",
                "combat": True,
                "enemies": ["PythonsPartisan"],
                "message": "You venture on",
            }
        ]

    def display(self):
        print(
            "You finally made it out of the dark cell. You look around in a dim light and cold environment. As you go forward, you notice eggshells. Welcome in the 'The Coldblooded Hatchery'. By mistake, you step on an egg and a big snake appears."
        )
