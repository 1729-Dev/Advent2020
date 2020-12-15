import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "day_05.data")

def find_seat(code):
    lower_row = 0
    upper_row = 127
    left = 0
    right = 7

    for char in code:
        row = int((lower_row + upper_row) / 2)
        column = int((left + right) / 2)
        if char == 'F':
            upper_row = row
            continue
        if char == 'B':
            row += 1
            lower_row = row
            continue
        if char == 'L':
            right = column
            continue
        if char == 'R':
            column += 1
            left = column
            continue
        raise Exception(f"Unknown code: {char}")

    return row * 8 + column

with open(filename) as f:
    lines = map(lambda x: (x.strip()), f.readlines())

    seats = []
    for line in lines:
        seats.append(find_seat(line))
    
    print(f"### max: {max(seats)}")
