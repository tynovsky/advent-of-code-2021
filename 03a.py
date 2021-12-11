import sys

counts = {}
l = 0
for line in sys.stdin:
    i = 0
    for d in line:
        if i not in counts:
            counts[i] = 0
        if d == "1":
            counts[i] += 1
        elif d == "0":
            counts[i] -= 1
        else:
            l = i
        i += 1

gamma, epsilon = 0, 0
for i in range(l):
    if counts[i] > 0:
        gamma += 2**(l - i -1)
    else:
        epsilon += 2**(l - i -1)

print(gamma)
print(epsilon)
print(gamma * epsilon)
