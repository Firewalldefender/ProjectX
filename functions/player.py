class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.attack = 10

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.max_health = self.max_health

    def is_alive(self):
        return self.health > 0
