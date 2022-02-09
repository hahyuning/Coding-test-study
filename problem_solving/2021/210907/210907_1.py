d = [0] * 100001
d[1] = 1
d[2] = 2
d[3] = 2
d[4] = 3
d[5] = 3
d[6] = 6

for i in range(7, 100001):
    d[i] = (d[i - 2] + d[i - 4] + d[i - 6]) % 1000000009

t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n])