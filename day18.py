class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def show(self):
        print(f"{self.name} - Damage: {self.damage}")
    def headshot(self):
        print(f"{self.name} can deal {self.damage} damage")

weapon1 = Weapon("Vandal", 160)
weapon2 = Weapon("Ghost", 80)
weapon3 = Weapon("Operator", 250)
weapon1.show()
weapon2.show()
weapon3.show()
weapon1.headshot()

class agent:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def show(self):
        print(f"{self.name} - {self.type}")
agent1 = agent("yoru", "duelist")
agent2 = agent("sage", "sentinal")
agent1.show()
agent2.show()