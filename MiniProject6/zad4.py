def odpluskw(f):
    def opakowujaca_funkcja(*args, **kwargs):
        print(f"Nazwa funkcji: {f.__name__}")
        print(f"Argumenty pozycyjne: {args}")
        print(f"Argumenty kluczowe: {kwargs}")

        wynik = f(*args, **kwargs)

        print(f"Wynik funkcji {f.__name__}: {wynik}")
        return wynik

    return opakowujaca_funkcja
@odpluskw
def dodaj(a,b):
    return a+b

dodaj(2,3)