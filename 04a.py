from sys import stdin

chosen = stdin.readline()

stdin.readline()

while line = stdin.readline().strip():
    while line != "":
        row = line.split()
        print(row)
        line = stdin.readline().strip()
