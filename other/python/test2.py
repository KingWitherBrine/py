from math import gcd
class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d
        if d < 0:
            self.n, self.d = -self.n, -self.d
        common = gcd(self.n, self.d)
        (self.n, self.d) = (self.n//common, self.d//common)
    def __add__(self, other):
        newn = self.n * other.d + self.d * other.n
        newd = self.d * other.d
        return Fraction(newn, newd)
    def __sub__(self, other):
        newn = self.n * other.d - self.d * other.n
        newd = self.d * other.d
        return Fraction(newn, newd)
    def __truediv__(self, other):
        newn = self.n * other.d
        newd = self.d * other.n
        return Fraction(newn, newd)
    def __mul__(self, other):
        newn = self.n * other.n
        newd = self.d * other.d
        return Fraction(newn, newd)
    def __repr__(self):
        return "{}/{}".format(int(self.n), int(self.d))
  
if __name__ == '__main__':
    s1, s2 = input().split()
    a, b = map(int, s1.split('/'))
    c, d = map(int, s2.split('/'))
    f1 = Fraction(a, b)
    f2 = Fraction(c, d)
    print(f1 + f2, f1 - f2, f1 * f2, f1 / f2)