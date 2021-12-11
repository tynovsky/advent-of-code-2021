from sys import stdin
from statistics import median

crabs = list(map(lambda x: int(x), stdin.readline().strip().split(",")))
result = sum(map(lambda x: abs(x - median(crabs)), crabs))

print(result)
