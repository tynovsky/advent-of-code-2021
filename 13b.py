import sys

dots = {}
for line in sys.stdin:
    line = line.strip()
    if line == '':
        break
    x,y = map(int, line.split(','))
    if (x,y) not in dots:
        dots[(x,y)] = 0
    dots[(x,y)] += 1

folds = []
for line in sys.stdin:
    axis, number = line.strip().split(' ')[2].split('=')
    axis = 0 if axis == 'x' else 1
    number = int(number)
    folds.append((axis, number))

# print(dots)
# print(folds)

def draw(dots):
    max_x = 0
    max_y = 0
    for (x,y) in dots:
        max_x = max(x, max_x)
        max_y = max(y, max_y)

    matrix = []
    for y in range(max_y+1):
        matrix.append([' '] * (max_x+1))
    for (x,y) in dots:
        matrix[y][x] = '#'
    for line in matrix:
        print(''. join(line))

def do_fold(dots, fold):
    axis, number = fold
    new_dots = {}
    for d in dots:
        if d[axis] < number:
            new_dots[d] = 1
            continue
        x,y = d
        # print("going to fold", x, y)
        if axis == 0:
            # print("folded", 2*number-x, y)
            new_dots[(2*number-x, y)] = 1
        else:
            # print("folded", x, 2*number-y)
            new_dots[(x, 2*number-y)] = 1
    return new_dots

for f in folds:
    dots = do_fold(dots, f)

draw(dots)
print()
# draw(dots)
# dots = do_fold(dots, folds[1])
# print()
# draw(dots)
# print(len(dots.keys()))
