class Player:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def show_info(self):
        print("name:", self.name)
        print("level:", self.level)
class Warrior(Player):
   
    def attack(self):
        print(self.name, "used Sword Slash!")

class mage(Player):

    def attack(self):
        print(self.name, "cast spell")

warrior1 = Warrior("Subhash", 21)
mage1 = mage("v" , 22)
warrior1.show_info()
warrior1.attack()
mage1.show_info()
mage1.attack()