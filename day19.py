class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def show(self):
        print(f"{self.name} - Damage: {self.damage}")


class Rifle(Weapon):

    def spray(self):
        print("Full auto firing!")


class Pistol(Weapon):
    pass


class Sniper(Weapon):
    pass


vandal = Rifle("Vandal", 160)
ghost = Pistol("Ghost", 80)
operator = Sniper("Operator", 250)

vandal.show()
ghost.show()
operator.show()

vandal.spray()