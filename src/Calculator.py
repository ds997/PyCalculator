
def addition(a, b):
    a = float(a)
    b = float(b)
    c = a + b
    return c


class MyCalculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result
