import sys

h_position = 0
depth = 0
aim = 0
for line in sys.stdin:
    command, value = line.split(' ')
    value = int(value)
    if command == 'forward':
        h_position += value
        depth += aim * value
    if command == 'up':
        aim -= value
    if command == 'down':
        aim += value

print(h_position * depth)
