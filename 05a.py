from sys import stdin
from pprint import pprint

seen_count = {}
intersections = 0
for line in stdin:
    line = line.strip()
    start, end = map(lambda x: list(map(lambda y: int(y), x.split(","))), line.split(" -> "))
    # print(start, end)
    if start[0] != end[0] and end[1] != start[1]:
        continue
    print(start, end)
    for i in range(min(start[0], end[0]), max(start[0], end[0])+1):
        for j in range(min(start[1], end[1]), max(start[1], end[1])+1):
            print(i, j)
            if (i, j) not in seen_count:
                seen_count[(i, j)] = 1
            else:
                seen_count[(i, j)] += 1
                if seen_count[(i, j)] == 2:
                    intersections += 1

pprint(seen_count)
print(intersections)




