from itertools import permutations as perms
from random import randint
names = ["Noah", "Eric", "Craig", "Xiaomeilv"]
print(list(perms(names, 2))[randint(0, len(names)-1)])
# print(list(perms(names, 2)))