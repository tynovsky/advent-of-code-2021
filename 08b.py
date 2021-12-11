import sys
from itertools import permutations

base_pattern = [
    'abcefg', 'cf', 'acdeg', 'acdfg',
    'bcdf', 'abdfg', 'abdefg', 'acf',
    'abcdefg', 'abcdfg'
]

def apply_perm(digit_str, perm):
    return ''.join(sorted(digit_str.translate(str.maketrans('abcdefg', perm))))
    
def is_permutation_valid(pattern, perm):
    perm_pattern = list(map(lambda x: apply_perm(x, perm), pattern))
    return set(perm_pattern) == set(base_pattern)

def read_number(digit_str, perm):
    return str(base_pattern.index(apply_perm(digit_str, perm)))

def perm2str(perm):
    str = 'abcdefg'
    return ''.join(map(lambda x: str[x], perm))

all_perms = list(map(perm2str, permutations(range(7))))
sum = 0
for line in sys.stdin:
    line = line.strip()
    signal_pattern, four_digits = line.split(' | ')
    signal_pattern = signal_pattern.split(' ')
    four_digits = four_digits.split(' ')

    for perm in all_perms:
        if is_permutation_valid(signal_pattern, perm):
            sum += int(''.join(map(lambda x: read_number(x, perm), four_digits)))
            break

print(sum)
