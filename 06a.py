from sys import stdin

fish = list(map(lambda x: int(x), stdin.readline().strip().split(",")))

round = 0
while True:
    round += 1
    new_count = 0
    for i,f in enumerate(fish):
        fish[i] = f-1 if f > 0 else 6
        if f == 0:
            new_count += 1
    
    fish += [8] * new_count
    print(round)
    print(fish)

    if round == 80:
        print(len(fish))
        break



