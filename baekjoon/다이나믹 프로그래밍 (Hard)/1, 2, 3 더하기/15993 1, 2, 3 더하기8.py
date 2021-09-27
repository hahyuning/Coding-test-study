d = [[0] * 100001 for _ in range(2)]
odd = 1
even = 0
d[odd][1] = 1
d[odd][2], d[even][2] = 1, 1
d[odd][3], d[even][3] = 2, 2

for i in range(4, 100001):
    d[odd][i] = (d[even][i - 1] + d[even][i - 2] + d[even][i - 3]) % 1000000009
    d[even][i] = (d[odd][i - 1] + d[odd][i - 2] + d[odd][i - 3]) % 1000000009

t = int(input())
for _ in range(t):
    n = int(input())
    print(d[odd][n], d[even][n])
