# local modules
import util
import levels

# other modules
import random


class Addition:
    def __init__(self, level):
        # all questions take lists as parameters which are then used to pick a random number
        self.level = level
        self.a = self._gen_var(True)
        self.b = self._gen_var(False)
        self.ans = self._calc_ans()

    def __str__(self):
        return f'{self.a} + {self.b}'

    def _gen_var(self, first):
        target = levels.add_values[self.level - (1 * int(first))]
        return target[random.randint(0, len(target) - 1)]

    def _calc_ans(self):
        return self.a + self.b


class Subtraction(Addition):
    def __str__(self):
        return f'{max(self.a, self.b)} - {min(self.a, self.b)}'

    def _gen_var(self, first):
        target = levels.add_values[self.level - (1 * int(first)) - 1]
        return target[random.randint(0, len(target) - 1)]
    
    def _calc_ans(self):
        return max(self.a, self.b) - min(self.a, self.b)


class NegativeSubtraction(Subtraction):
    def __str__(self):
        return f'{min(self.a, self.b)} - {max(self.a, self.b)}'

    def _gen_var(self, first):
        target = levels.add_values[self.level - (1 * int(first)) - 2]
        return target[random.randint(0, len(target) - 1)]
        
    def _calc_ans(self):
        return min(self.a, self.b) - max(self.a, self.b)


class Multiplication(Addition):
    def __str__(self):
        return f'{self.a} × {self.b}'

    def _gen_var(self, first):
        target = levels.mult_values[self.level - (1 * int(first))]
        return target[random.randint(0, len(target) - 1)]
        
    def _calc_ans(self):
        return self.a * self.b


class Division(Addition):
    def __str__(self):
        return f'{self.a} ÷ {self.b}'

    def _gen_var(self, first):
        target = levels.mult_values[self.level - (1 * int(first)) - 1]
        return target[random.randint(0, len(target) - 1)]

    def _calc_ans(self):
        return self.a / self.b


class Power(Addition):
    def __str__(self):
        return f'{self.a}{util.superscript(self.b)}'

    def _calc_ans(self):
        return pow(self.a, self.b)


class Root(Power):
    def __str__(self):
        return f'{util.superscript(self.b) if self.b != 2 else ""}√{self.a}'

    def _calc_ans(self):
        return pow(self.a, 1/self.b)


class Triangle(Addition):
    def __str__(self):
        return f'A right-angled triangle has two sides of lengths {self.a} and {self.b} with an unknown hypotenuse.' \
               f'\nWhat is the area of this triangle?'

    def _gen_var(self, first):
        target = levels.mult_values[self.level - (1 * int(first)) - 4]
        return target[random.randint(0, len(target) - 1)]

    def _calc_ans(self):
        return (self.a * self.b) / 2


class SquareArea(Addition):
    def __str__(self):
        return f'A rectangle has two sides of lengths {self.a} and {self.b}\nWhat is the area of this rectangle?'

    def _gen_var(self, first):
        target = levels.mult_values[self.level - (1 * int(first)) - 2]
        return target[random.randint(0, len(target) - 1)]

    def _calc_ans(self):
        return self.a * self.b


class SquarePerimeter(SquareArea):
    def __str__(self):
        return f'A rectangle has two sides of lengths {self.a} and {self.b}\nWhat is the perimeter of this rectangle?'

    def _gen_var(self, first):
        target = levels.mult_values[self.level - (1 * int(first)) - 3]
        return target[random.randint(0, len(target) - 1)]

    def _calc_ans(self):
        return 2 * (self.a * self.b)


class CircleArea:
    def __init__(self, a):
        self.a = a[random.randint(0, len(a) - 1)]
        self.ans = self._calc_ans()

    def __str__(self):
        return f'A circle\'s radius is {self.a} long.\nWhat is the area of this circle?'

    def _calc_ans(self):
        return pow(self.a, 2)


class CirclePerimeter(CircleArea):
    def __str__(self):
        return f'A circle\'s radius is {self.a} long.\nWhat is the perimeter of this circle?'

    def _gen_var(self, first):
        target = levels.mult_values[self.level - (1 * int(first)) - 4]
        return target[random.randint(0, len(target) - 1)]

    def _calc_ans(self):
        return 2 * self.a


'''
    QUESTION EXPLANATIONS
    
    Addition: Addition. 
        a + b = c
    Subtraction: Subtraction. Always results in a positive or zero answer. 
        a - b = c, where a > b.
    NegativeSubtraction: Subtraction. Always results in a negative or zero answer. 
        a - b = c, where a < b.
    Multiplication: Multiplication.
        a * b = c
    Division: Division. Given inputs will always result in an integer answer.
        a / b = c, where a > b and c = int
'''