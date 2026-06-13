class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b


print(Calculator.add(10, 5))
print(Calculator.subtract(10, 5))
print(Calculator.multiply(10, 5))