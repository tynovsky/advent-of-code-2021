from sys import stdin
from pprint import pprint

taken = list(map(lambda x: int(x), stdin.readline().strip().split(",")))

tables = []
table = None
for line in stdin:
    line = line.strip()
    if line == "":
        table = []
        tables.append(table)
        continue
    row = list(map(lambda x: [int(x), False], line.split()))
    table += row

print(tables)


def is_winning(table, i):
    n = len(table)
    row_length = int(n ** (1/2))
    col = i % row_length
    # check row
    start = i - col
    end = i - col + row_length
    fullrow = True
    print()
    for j in range(start, end):
        print(table[j][0])
        fullrow = fullrow and table[j][1]
    if fullrow:
        return True
    fullcol = True
    for j in range(col, n, row_length):
        print(table[j][0])
        fullcol = fullcol and table[j][1]
    if fullcol:
        return True

    return False

def sum_nonmarked(table):
    s = 0
    for e in table:
        if e[1] == False:
            s += e[0]
    return s

for n in taken:
    for i, table in enumerate(tables):
        for j, element in enumerate(table):
            if element[0] == n:
                element[1] = True
            if is_winning(table, j):
                print("Win: ",  i)
                s = sum_nonmarked(table)
                print("Tblsum: ", s)
                print("Result: ", s * table[j][0])
                exit(0)
