from sys import stdin
from statistics import median
from statistics import mean

crabs = list(map(lambda x: int(x), stdin.readline().strip().split(",")))
crabs_mean = round(mean(crabs))
crabs = list(map(lambda x: abs(x - crabs_mean), crabs))
result = sum(map(lambda x: int(x*(x+1)//2), crabs))


print(result)
