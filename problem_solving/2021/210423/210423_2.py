t = int(input())
d = [0] * 10001

for i in range(1, 4):
    for j in range(10001):
        if j - i >= 0:
            d[j] += d[j - i]

for _ in range(t):
    n = int(input())
    print(d[n])