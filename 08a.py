import sys

count = 0
for line in sys.stdin:
    line = line.strip()
    signal_pattern, four_digits = line.split(' | ')
    for digit in four_digits.split(' '):
        if len(digit) in [2,3,4,7]:
            count += 1

print(count)
