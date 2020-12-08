import os

def filter_fctn(_):
    return sum(list(_)) == 2020

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "day_03.data")

total_trees = 1

slopes = [(1,1), (3,1), (5,1), (7,1), (1, 2)]
for slope in slopes:
    with open(filename) as f:
        lines = f.readlines()
        lines = list(map(lambda x: (x.strip()), lines))
        x_total = 0
        trees = 0

        for index in range(slope[1], len(lines), slope[1]):
            line = lines[index]

            x_total += slope[0]
            x_pos = x_total % len(line) 

            if (line[x_pos] == '#'):
                trees += 1

        print(f"slope: {slope} trees: {trees}")
        total_trees = total_trees * trees

print(f"total trees multiplied: {total_trees}")