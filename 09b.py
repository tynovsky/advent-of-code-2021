import sys

def neighbors(x, y, rows, cols):
    result = []
    if x > 0:
        result.append((x-1, y))
    if x < rows-1:
        result.append((x+1, y))
    if y > 0:
        result.append((x, y-1))
    if y < cols -1:
        result.append((x, y+1))
    return result

def g(m, coords):
    return m[coords[0]][coords[1]]

def is_low(m, coords, rows, cols):
    nei = neighbors(*coords, rows, cols)
    lowernei = list(filter(lambda x: g(m, x) <= g(m, coords), nei))
    return len(lowernei) == 0

def fill_basin(m, coords, rows, cols):
    result = set()
    to_process = [coords]
    while len(to_process) > 0:
        p = to_process.pop()
        if p in result:
            continue
        if g(m, p) == 9:
            continue
        result.add(p)
        to_process += neighbors(p[0], p[1], rows, cols)
    return result

matrix = []
rows, cols = 0, 0
for line in sys.stdin:
    cols = len(line) - 1
    rows += 1
    matrix.append(list(map(int, (list(line.strip())))))

low_points = []
for i in range(rows):
    for j in range(cols):
        if is_low(matrix, (i, j), rows, cols):
            low_points.append((i, j))

max_three = [0, 0, 0]
for p in low_points:
    basin = fill_basin(matrix, p, rows, cols)
    max_three = sorted(max_three + [len(basin)])[1:4]

print(max_three[0]*max_three[1]*max_three[2])
