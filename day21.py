class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


class Rifle:
    def attack(self):
        print("spraying bullets")

class Sniper:
    def attack(self):
        print("one shot kill")

class Pistol:
    def attack(self):
        print("quick tap")


vandal = Rifle()
operator = Sniper()
ghost = Pistol()

weapons = [vandal, operator, ghost]
for weapon in weapons:
    weapon.attack()

class Jett:
    def ability(self):
        print("updraft")

class Sage:
    def ability(self):
        print("healing")

class Phoenix:
    def ability(self):
        print("fire wall")

jett = Jett()
sage = Sage()
phoenix = Phoenix()


agents = [jett, sage, phoenix ]


for agent in agents:
    agent.ability()