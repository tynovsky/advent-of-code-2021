import sys

h_position = 0
depth = 0
for line in sys.stdin:
    command, value = line.split(' ')
    value = int(value)
    if command == 'forward':
        h_position += value
    if command == 'up':
        depth -= value
    if command == 'down':
        depth += value

print(h_position * depth)
