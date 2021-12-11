import sys

def neighbors(x, y, rows, cols):
    result = []
    xs = [x]
    ys = [y]
    if x > 0:
        xs.append(x-1)
    if x < rows-1:
        xs.append(x+1)
    if y > 0:
        ys.append(y-1)
    if y < cols -1:
        ys.append(y+1)

    for i in xs:
        for j in ys:
            if (x, y) != (i, j):
                yield (i, j)


def flashes(matrix):
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element > 9:
                yield (i, j)

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end="")
        print()


matrix = []
rows, cols = 0, 0
for line in sys.stdin:
    cols = len(line) - 1
    rows += 1
    matrix.append(list(map(int, (list(line.strip())))))


print_matrix(matrix)


total_flashed_count = 0
for step in range(1, 1001):
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            matrix[i][j] += 1

    flashed = set()
    to_flash = list(flashes(matrix))
    print(to_flash)
    while len(to_flash) > 0:
        (x, y) = to_flash.pop()
        # print("flash", (x, y))
        if (x, y) in flashed:
            continue
        flashed.add((x, y))
        for (i, j) in neighbors(x, y, rows, cols):
            matrix[i][j] += 1
            if matrix[i][j] > 9:
                to_flash.append((i, j))

    for (i, j) in flashed:
        matrix[i][j] = 0

    print("After step", step)
    print_matrix(matrix)
    total_flashed_count += len(flashed)
    print(total_flashed_count)

    total = 0
    for row in matrix:
        total += sum(row)

    if total == 0:
        break
