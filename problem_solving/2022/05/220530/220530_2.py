import math

n = int(input())
d = [4] * (n + 1)
d[0] = 0
d[1] = 1

for i in range(2, n + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        d[i] = min(d[i], d[i - j ** 2] + 1)

print(d[n])