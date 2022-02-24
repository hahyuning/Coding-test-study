h, y = map(int, input().split())
d = [0] * (y + 1)
d[0] = h

for i in range(1, y + 1):
    if i >= 5:
        d[i] = max(d[i - 1] * 1.05, d[i - 3] * 1.2, d[i - 5] * 1.35)
    elif i >= 3:
        d[i] = max(d[i - 1] * 1.05, d[i - 3] * 1.2)
    else:
        d[i] = d[i - 1] * 1.05
    d[i] = int(d[i])

print(d[y])
