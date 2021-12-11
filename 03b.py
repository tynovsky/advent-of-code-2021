import sys

lines = [line.rstrip() for line in sys.stdin.readlines()]

oxy_list = lines
oxy = []
i = 0
while len(oxy_list) > 1:
    m = 1 if len(list(filter(lambda x: x[i] == "1", oxy_list))) >= len(oxy_list) / 2 else 0
    oxy_list = list(filter(lambda x: int(x[i]) == m, oxy_list))
    oxy.append(m)
    i += 1

for n in oxy_list[0][i:]:
    oxy.append(n)

oxy_result = 0
for e, n in enumerate(reversed(oxy)):
    oxy_result += n * 2**e
print(oxy_result)


co2_list = lines
co2 = []
i = 0
while len(co2_list) > 1:
    m = 0 if len(list(filter(lambda x: x[i] == "0", co2_list))) <= len(co2_list) / 2 else 1
    co2_list = list(filter(lambda x: int(x[i]) == m, co2_list))
    co2.append(m)
    i += 1

for n in co2_list[0][i:]:
    co2.append(int(n))

co2_result = 0
for e, n in enumerate(reversed(co2)):
    co2_result += n * 2**e

print(co2_result)

print(co2_result * oxy_result)
