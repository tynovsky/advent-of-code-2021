import sys

result = 0
prev = [
    int(sys.stdin.readline()),
    int(sys.stdin.readline()),
    int(sys.stdin.readline()),
]

for line in sys.stdin:
    n = int(line)
    p = prev.pop(0)
    if n > p:
        result += 1
    prev.append(n)

print(result)
