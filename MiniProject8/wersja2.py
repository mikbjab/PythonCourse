import argparse
import math
import random
import time


class Ulamek:
    __slots__ = ('licznik', 'mianownik')
    def __init__(self, a, b):
        assert b != 0
        skracanie = math.gcd(int(a), int(b))
        self.licznik = a / skracanie
        self.mianownik = b / skracanie
        if b < 0:
            self.licznik *= (-1)
            self.mianownik *= (-1)

    def __add__(self, other):
        licznik1 = other.licznik * self.mianownik
        mianownik1 = other.mianownik * self.mianownik
        licznik2 = self.licznik * other.mianownik
        return Ulamek(licznik1 + licznik2, mianownik1)

    def __sub__(self, other):
        licznik1 = other.licznik * self.mianownik
        mianownik1 = other.mianownik * self.mianownik
        licznik2 = self.licznik * other.mianownik
        return Ulamek(licznik2 - licznik1, mianownik1)

    def __mul__(self, other):
        return Ulamek(self.licznik * other.licznik, self.mianownik * other.mianownik)

    def __truediv__(self, other):
        return Ulamek(self.licznik * other.mianownik, self.mianownik * other.licznik)

    def __str__(self):
        return str(self.licznik) + "/" + str(self.mianownik)

    def __repr__(self):
        return "Ulamek(" + str(self.licznik) + "/" + str(self.mianownik) + ")"

    def __ge__(self, other):
        return self.licznik * other.mianownik >= self.mianownik * other.licznik

    def __gt__(self, other):
        return self.licznik * other.mianownik > self.mianownik * other.licznik

    def __le__(self, other):
        return self.licznik * other.mianownik <= self.mianownik * other.licznik

    def __lt__(self, other):
        return self.licznik * other.mianownik < self.mianownik * other.licznik

    def __eq__(self, other):
        return self.licznik == other.licznik and self.mianownik == other.mianownik


parser = argparse.ArgumentParser()
parser.add_argument("n", type=int)
parser.add_argument("k", type=int)
args = parser.parse_args()
n = args.n
k = args.k
print(n, k)

start = time.time()
list_of_fractions = []
for i in range(n):
    list_of_fractions.append(Ulamek(random.randint(1, 13), random.randint(1, 13)))

for i in range(k):
    list_of_fractions[i % n] = list_of_fractions[i % n] - list_of_fractions[i % n - 1]

end = time.time()
print(end - start)
