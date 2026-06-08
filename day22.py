from abc import ABC, abstractmethod


class Weapon(ABC):

    @abstractmethod
    def attack(self):
        pass


class Rifle(Weapon):

    def attack(self):
        print("Spraying bullets")


class Sniper(Weapon):

    def attack(self):
        print("One shot kill")

vandal = Rifle()
operator = Sniper()

vandal.attack()
operator.attack()

from abc import ABC, abstractmethod


class Agent(ABC):

    @abstractmethod
    def ability(self):
        pass


class Jett(Agent):

    def ability(self):
        print("updraft")

class Phoenix(Agent):

    def ability(self):
        print("fire wall")

class Sage(Agent):

    def ability(self):
        print("healing")

jett = Jett()
sage = Sage()
phoenix = Phoenix()

agents = [jett, sage, phoenix]

for agent in agents:
    agent.ability()