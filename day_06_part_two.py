import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "day_06.data")

with open(filename) as f:
    lines = map(lambda x: (x.strip()), f.readlines())
    groups = []
    group = ''
    counts = []
    count = 0
    for line in lines:
        if len(line) > 0:
            group = group + line
            count += 1
            continue
        groups.append(group)
        group = ''
        counts.append(count)
        count = 0
    groups.append(group)
    counts.append(count)

    total = 0
    for i in range(len(groups)):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if groups[i].count(char) == counts[i]:
                total += 1

    print(f"total: {total}")
