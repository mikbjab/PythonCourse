import operator
from itertools import starmap, chain, repeat, tee
from functools import partial

def transform_iterator(iterator):
    it1, it2 = tee(iterator)
    final_final_iterator=map(lambda x: (x[0][0],x[0][1],x[1]),zip(it2, starmap(partial(operator.pow), it1)))
    return final_final_iterator

# Przykład użycia
pairs = [(2, 3), (4, 2), (5, 2)]
transformed_iterator = transform_iterator(iter(pairs))

for item in transformed_iterator:
    print(item)