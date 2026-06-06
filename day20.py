class BankAccount:
    def __init__(self, balance):
        self.balance = balance


account = BankAccount(1000)

account.balance = -50000

print(account.balance)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def show_balance(self):
        
        print(account.__balance)
account = BankAccount(1000)

account.show_balance()

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount

        else:
            print("Insufficient Balance")


account = BankAccount(1000)

account.deposit(500)

account.withdraw(300)

account.show_balance()


class Player:
    def __init__(self, health):
        self.__health = health

    def show__health(self):
        print("health: ", self.__health)

    def heal(self, amount):
        self.__health += amount

    def take_damage(self, damage):
        self.__health -= damage

        if self.__health < 0:
            self.__health = 0

player = Player(100)

player.take_damage(30)

player.heal(20)

player.show__health()