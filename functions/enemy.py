class Enemy:
    def __init__(self, name, health, difficulty):
        self.name = name
        self.health = health
        self.difficulty = difficulty
        self.attack = 10

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0
