class Player:

    def __init__(self, name, level):
        self.name = name
        self.level = level
player1 = Player("Subhash", 21)
player2 = Player("V", 25)

print(player1.name, player2.name)
print(player1.level, player2.level)


class Player:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def show_info(self):
        print("Name:", self.name)
        print("Level:", self.level)
player1 = Player("Subhash", 21)
player2 = Player("V", 25)
player1.show_info()
player2.show_info()