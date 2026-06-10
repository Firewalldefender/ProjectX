from base_level import Level


class intro(Level):
    def __init__(self):
        super().__init__(name="Intro", description="You wake up in a dark room")

        self.choices = [
            {"text": "Enter dungeon", "next": "level2", "message": "You chose Level 2"}
        ]

    def display(self):
        pass

    def handle_choice(self):
        pass
