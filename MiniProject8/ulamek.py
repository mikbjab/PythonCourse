import math


class Ulamek:
    def __init__(self,a,b):
        assert b != 0
        skracanie=math.gcd(int(a),int(b))
        self.licznik=a/skracanie
        self.mianownik=b/skracanie
        if b<0:
            self.licznik*=(-1)
            self.mianownik*=(-1)

    def __add__(self, other):
        licznik1=other.licznik*self.mianownik
        mianownik1=other.mianownik*self.mianownik
        licznik2=self.licznik*other.mianownik
        return Ulamek(licznik1+licznik2,mianownik1)

    def __sub__(self, other):
        licznik1 = other.licznik * self.mianownik
        mianownik1 = other.mianownik * self.mianownik
        licznik2 = self.licznik * other.mianownik
        return Ulamek(licznik2 - licznik1, mianownik1)

    def __mul__(self, other):
        return Ulamek(self.licznik*other.licznik,self.mianownik*other.mianownik)

    def __truediv__(self, other):
        return Ulamek(self.licznik*other.mianownik,self.mianownik*other.licznik)

    def __str__(self):
        return str(self.licznik)+"/"+str(self.mianownik)

    def __repr__(self):
        return "Ulamek(" + str(self.licznik) + "/" + str(self.mianownik) +")"

    def __ge__(self, other):
        return self.licznik*other.mianownik>=self.mianownik*other.licznik

    def __gt__(self, other):
        return self.licznik * other.mianownik > self.mianownik * other.licznik

    def __le__(self, other):
        return self.licznik * other.mianownik <= self.mianownik * other.licznik

    def __lt__(self, other):
        return self.licznik * other.mianownik < self.mianownik * other.licznik

    def __eq__(self, other):
        return self.licznik==other.licznik and self.mianownik==other.mianownik






