from levels.base_level import Level
from rich import print

# The Poisonous Pathways


class Level3(Level):
    def __init__(self):
        super().__init__(name="level3")

        self.choices = [
            {
                "text": "The Poisonous Pathways",
                "next": "victory",
                "combat": True,
                "enemies": ["PythonsPartisan"],
                "message": "You venture on",
            }
        ]

    def display(self):
        print(
            "The hatchery stays behind, but the danger only comes closer. With a pungent smell in the air and statues of cobras, you know you've reached 'The Poisonous Pathways'."
        )
