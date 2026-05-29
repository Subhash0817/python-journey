class Player:

    def __init__(self, name, level):
        self.name = name
        self.level = level
player1 = Player("Subhash", 21)
player2 = Player("V", 25)

print(player1.name, player2.name)
print(player1.level, player2.level)


class Player:

    def __init__(self, name, level, health, damage):
        self.name = name
        self.level = level
        self.health = health
        self.damage = damage
    def take_damage(self, amount):
        self.health -= amount
        print(self.name, "took", amount, "damage")
    def heal(self, amount):
        self.health += amount
        print(self.name, "healed", amount, "health")
    def level_up(self):
            self.level += 1
            print(self.name, "leveled up!")
    def show_info(self):
        print("Name:", self.name)
        print("Level:", self.level)
        print("health:", self.health)
        print("damage:", self.damage)
        

        
player1 = Player("Subhash", 21, 100, 160)

player1.show_info()
player1.take_damage(20)
player1.heal(10)
player1.level_up()

player1.show_info()