import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "day_06.data")

with open(filename) as f:
    lines = map(lambda x: (x.strip()), f.readlines())
    groups = []
    group = ''
    for line in lines:
        if len(line) > 0:
            group = group + line
            continue
        groups.append(group)
        group = ''
    groups.append(group)

    group_total = 0
    for group in groups:
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if char in group:
                group_total += 1
    print(f"group_total: {group_total}")
