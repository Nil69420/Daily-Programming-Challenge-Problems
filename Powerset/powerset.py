from itertools import combinations
sets = [1, 2, 3]
for i in range(0, len(sets) + 1):
    for x in combinations(sets, i):
        print(list(''.join(map(str, x))), end=" ")

