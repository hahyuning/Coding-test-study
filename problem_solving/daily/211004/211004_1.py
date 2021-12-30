n = int(input())
a = []
i = 0
while True:
    tmp = ((i * (i + 1) * (2 * i + 1)) // 6 + (i * (i + 1)) // 2) // 2
    if tmp > n:
        break
    a.append(tmp)
    i += 1

# d[i]: 구슬이 i개 있을 때 만들 수 있는 사면체의 최소 갯수
d = [300000] * (n + 1)
for i in range(1, n + 1):
    for x in a:
        if x == i:
            d[i] = 1
            break
        if x > i:
            break
        d[i] = min(d[i], d[i - x] + 1)
print(d[n])