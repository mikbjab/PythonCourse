import math
from functools import reduce

lista_napisow = "Ala zaadaptowała strasznie zabawnego kota".split()

# zadanie 1
lista_prawie_dlugosci = list(map(lambda s: (len(s)//2) * 2, lista_napisow))
print(lista_prawie_dlugosci)

# zadanie 2 -> reszta z dzielenia przez 17 (zakladam ze 0 to liczba naturalna)
lista_reszt=list(map(lambda x: (x*x) % 17, range(20)))
print(lista_reszt)


# zadanie 3 -> kwadraty liczb mniejszych niz 100 i mające dwie 1 pod rzad
def dobra_liczba(n):
    if math.floor(math.sqrt(n))**2 != n:
        return False
    number = str(n)
    for i in range(len(number)-1):
        if number[i] == "1" and number[i+1] == "1":
            return True
    return False


lista_dobrych_liczb = list(filter(dobra_liczba, range(10000)))
print(lista_dobrych_liczb)

# zadanie 4 -> silnia

def silnia(n):
    return reduce(lambda x,y: x*y,range(1,n+1))

print(silnia(5))

# zadanie 5 -> sumuj

def sumuj(lista_liczb):
    return reduce(lambda x,y: [x[0]+y,x[1]] if y%2==0 else [x[0],x[1]+y],lista_liczb,[0,0])


