class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def show(self):
        print(f"{self.name} - Damage: {self.damage}")

weapon1 = Weapon("Vandal", 160)
weapon1.show()