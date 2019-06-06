from math import sqrt

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @ staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


def main():
    a, b, c = 2, 3, 4
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        print(t.area())
    else:
        print('No triangle formed')


if __name__ == '__main__':
    main()
