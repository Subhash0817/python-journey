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


class Player:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def show_info(self):
        print("name:", self.name)
        print("level:", self.level)
    def attack(self):
        print(self.name, "attacked")
class Warrior(Player):
   
    def attack(self):
        print(self.name, "used Sword Slash!")

class mage(Player):

    def attack(self):
        print(self.name, "cast firball")

warrior1 = Warrior("Subhash", 21)
mage1 = mage("v" , 22)

warrior1.attack()

mage1.attack()


class Player:

    def __init__(self, name, level):
        self.name = name
        self.level = level

class Warrior(Player):

    def __init__(self, name, level, weapon):
        super().__init__(name, level)
        self.weapon = weapon
warrior1 = Warrior("Subhash", 21, "Vandal")
print(warrior1.name)
print(warrior1.level)
print(warrior1.weapon)


"""Mini RPG Character System """

class Player:

    def __init__(self, name, level):
        self.name = name
        self.level = level
class Warrior(Player):

    def __init__(self, name, level, weapon, heal):
        super().__init__(name, level)
        self.weapon = weapon
        self.heal = heal
    def attack(self):
        print(self.name, "used Sword Slash!")

class Mage(Player):

    def __init__(self, name, level, spell, heal):
        super().__init__(name, level)
        self.spell = spell
        self.heal = heal

    def attack(self):
        print(self.name, "cast", self.spell)

warrior1 = Warrior("Subhash", 21, "vandal", 200)
mage1 = Mage("v" , 22 , "lantherpagidi", 150)

warrior1.attack()

mage1.attack()
