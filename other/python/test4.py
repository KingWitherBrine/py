from math import gcd

class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d
        common = gcd(self.n, self.d)
        (self.n, self.d) = (self.n//common, self.d//common)
    def __gt__(self, other):
        num1 = self.n * other.d
        num2 = other.n * self.d
        return num1 > num2
    def __ge__(self, other):
        num1 = self.n * other.d
        num2 = other.n * self.d
        return num1 >= num2
    def __lt__(self, other):
        num1 = self.n * other.d
        num2 = other.n * self.d
        return num1 < num2
    def __le__(self, other):
        num1 = self.n * other.d
        num2 = other.n * self.d
        return num1 <= num2
    def __eq__(self, other):
        num1 = self.n * other.d
        num2 = other.n * self.d
        return num1 == num2
    def __ne__(self, other):
        num1 = self.n * other.d
        num2 = other.n * self.d
        return num1 != num2
    def __repr__(self):
        return "{}/{}".format(int(self.n), int(self.d))

if __name__ == '__main__':
    s1, s2 = input().split()
    a, b = map(int, s1.split('/'))
    c, d = map(int, s2.split('/'))
    f1 = Fraction(a, b)
    f2 = Fraction(c, d)
    print(f1 > f2, f1 >= f2, f1 < f2, f1 <= f2, f1 == f2, f1 != f2)