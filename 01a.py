import sys

result = 0
prev = int(sys.stdin.readline())
for line in sys.stdin:
    n = int(line)
    if n > prev:
        result += 1
    prev = n

print(result)
