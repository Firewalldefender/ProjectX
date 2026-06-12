class Enemy:
    def __init__(self, name, health, difficulty, attack):
        self.name = name
        self.health = health
        self.max_health = health
        self.difficulty = difficulty
        self.attack = attack
        self.waves = 1
        self.max_waves = 1

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        if self.health == 0 and self.waves > 0:
            self.waves -= 1

    def is_active(self):
        return self.health > 0 or self.waves > 0

    def is_defeated(self):
        return self.health == 0

    def reset(self):
        self.health = self.max_health