import os
import itertools
import time

def filter_fctn(_):
    return sum(list(_)) == 2020

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "day_02.data")

def min_max_password_check(x):
    lower = int(x[0][0])
    upper = int(x[0][1])
    test_char = x[1]
    password = x[2]
    char_count = password.count(test_char)

    return lower <= char_count and char_count <= upper

def positional_password_check(x):
    left = int(x[0][0]) - 1
    right = int(x[0][1]) - 1
    test_char = x[1]
    password = x[2]
    a = password[left] == test_char
    b = password[right] == test_char

    return a ^ b

with open(filename) as f:
    lines = map(lambda x: (x.strip().split()), f.readlines())
    lines = map(lambda x: (x[0].split('-'), x[1][0], x[2]), lines)
    good_passwords = filter(min_max_password_check, lines)
    print(f"min max good: {len(list(good_passwords))}")

with open(filename) as f:
    lines = map(lambda x: (x.strip().split()), f.readlines())
    lines = map(lambda x: (x[0].split('-'), x[1][0], x[2]), lines)
    good_passwords = filter(positional_password_check, lines)
    print(f"positional good: {sum(1 for _ in good_passwords)}")
