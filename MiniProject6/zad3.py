from itertools import chain, repeat


def zrob_drzewo(n, iterable):
    it = iter(iterable)

    def pomocnicza(ilosc):
        if ilosc == 0:
            return None
        else:
            lewe = pomocnicza(ilosc // 2)
            korzen = next(it)
            prawe = pomocnicza(ilosc - ilosc // 2 - 1)
            return (lewe, korzen, prawe)

    return pomocnicza(n)

print(zrob_drzewo(7,"alakota"))


def obejdź_yield(drzewo, preorder=False, inorder=False, postorder=False):
    if not (preorder ^ inorder ^ postorder) or (preorder and inorder and postorder):
        raise ValueError("Dokładnie jeden z argumentów preorder, inorder, postorder musi być prawdą.")

    def pomocnicza(drzewo):
        if drzewo is not None:
            if preorder:
                yield drzewo[1]
            yield from pomocnicza(drzewo[0])
            if inorder:
                yield drzewo[1]
            yield from pomocnicza(drzewo[2])
            if postorder:
                yield drzewo[1]

    return pomocnicza(drzewo)


def obejdź(drzewo, preorder=False, inorder=False, postorder=False):
    if not (preorder ^ inorder ^ postorder) or (preorder and inorder and postorder):
        raise ValueError("Dokładnie jeden z argumentów preorder, inorder, postorder musi być prawdą.")

    def pomocnicza(drzewo):
        if drzewo is not None:
            if preorder:
                yield drzewo[1]
            yield from pomocnicza(drzewo[0])
            if inorder:
                yield drzewo[1]
            yield from pomocnicza(drzewo[2])
            if postorder:
                yield drzewo[1]

    return chain.from_iterable(repeat(x, 1) for x in pomocnicza(drzewo))

print(list(obejdź(zrob_drzewo(7,"alakota"),postorder=True)))