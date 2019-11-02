
def addition(a, b):
    a = float(a)
    b = float(b)
    c = a + b
    return c


def subtraction(a, b):
    a = float(a)
    b = float(b)
    c = b - a
    return c


def multiplication(a, b):
    a = float(a)
    b = float(b)
    c = a * b
    return c


class MyCalculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result