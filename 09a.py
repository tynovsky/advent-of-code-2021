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

matrix = []
rows, cols = 0, 0
for line in sys.stdin:
    cols = len(line) - 1
    rows += 1
    matrix.append(list(map(int, (list(line.strip())))))

risk = 0
for i in range(rows):
    for j in range(cols):
        if is_low(matrix, (i, j), rows, cols):
            risk += g(matrix, (i, j)) + 1

print(risk)
