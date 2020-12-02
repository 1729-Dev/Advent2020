import os
import itertools
import time

def filter_fctn(_):
    return sum(list(_)) == 2020

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "day_01.data")

with open(filename) as f:
    lines = [int(x) for x in f]
    combos = itertools.combinations(lines, 3)

    found = list(tuple())
    tic = time.time()
    for combo in combos:
        if (combo[0] + combo[1] + combo[2] == 2020):
            found.append(combo)
    toc = time.time()
    print(f"for loop time: {(toc - tic) * 1000} milliseconds")
    for f in found:
        print(f"for loop combo: {f} with mult: {f[0] * f[1] * f[2]}")

with open(filename) as f:
    lines = [int(x) for x in f]
    combos = itertools.combinations(lines, 3)

    tic = time.time()
    filtered_combos = filter(filter_fctn, combos)
    toc = time.time()
    print(f"filter time: {(toc - tic) * 1000} milliseconds")
    for f in filtered_combos:
        print(f"filtered_combo: {f} with mult: {f[0] * f[1] * f[2]}")
