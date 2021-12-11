from sys import stdin

fish = list(map(lambda x: int(x), stdin.readline().strip().split(",")))

counts = [0] * 9
for f in fish:
    counts[f] += 1

round = 0
while True:
    round += 1
    new = counts[0]
    for i in range(8):
        counts[i] = counts[i+1]
    counts[8] = new
    counts[6] += new

    if round == 256:
        print(sum(counts))
        break



