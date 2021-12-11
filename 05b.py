from sys import stdin

def cmp(a, b):
    return int(a > b) - int(a < b)

def points_between(start, end):
    i_step = cmp(end[0], start[0])
    j_step = cmp(end[1], start[1])
    [i, j] = start

    while True:
        yield (i, j)
        if (i, j) == end:
            break
        i += i_step
        j += j_step

seen_count = {}
intersections = 0
for line in stdin:
    start, end = map(
        lambda x: tuple(
            map(lambda y: int(y), x.split(","))
        ),
        line.strip().split(" -> ")
    )
    for p in points_between(start, end):
        if p not in seen_count:
            seen_count[p] = 1
        else:
            seen_count[p] += 1
            if seen_count[p] == 2:
                intersections += 1

print(intersections)
