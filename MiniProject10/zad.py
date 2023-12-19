import math
import unittest
from unittest.mock import MagicMock, mock_open

import pytest as pytest


class Ulamek:
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

    def save(self,filename):
        with open(filename,"w") as file:
            file.write(f"{self.licznik}\n{self.mianownik}")

    @classmethod
    def load(cls,filename):
        with open(filename) as file:
            licznik=int(file.readline())
            mianownik=int(file.readline())
        return cls(licznik,mianownik)


@pytest.fixture
def mock_open_file(monkeypatch):
    m = mock_open()
    monkeypatch.setattr("builtins.open", m)
    return m

@pytest.mark.parametrize("ulamek1, ulamek2, expected", [
    (Ulamek(1, 2), Ulamek(1, 4), Ulamek(3, 4)),
    (Ulamek(3, 4), Ulamek(1, 4), Ulamek(1, 1)),
    (Ulamek(1, 3), Ulamek(2, 3), Ulamek(1, 1)),
    # Dodaj więcej przypadków testowych według potrzeb
])
def test_dodawanie_ulamkow(ulamek1, ulamek2, expected):
    wynik = ulamek1 + ulamek2
    assert wynik == expected

def test_zapis_do_pliku(mock_open_file):
    ulamek = Ulamek(3, 4)
    ulamek.save('test.txt')
    mock_open_file.assert_called_once_with('test.txt', 'w')
    handle = mock_open_file()
    handle.write.assert_called_once_with('3.0\n4.0')

def test_wczytaj_z_pliku(mock_open_file):
    mock_open_file(read_data='3.0\n4.0')
    ulamek = Ulamek.load('test.txt')
    assert ulamek.licznik == 3
    assert ulamek.mianownik == 4

