class Calculator:
    def __init__(self, x,  y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(x, y):
        return x.input1 - y.input2

    def mul(x, y):
        return x.input1 * y.input2

    def div(x, y):
        return x.input1  / y.input2


calc_sum = Calculator(1, 2)
print(calc_sum.add())
