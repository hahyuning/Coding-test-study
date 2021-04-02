n = int(input())
# d[n] : n을 1로 만드는 최소 횟수
# d[n] = min(d[n - 1], d[n // 3], d[n // 2]) + 1
d = [0] * 1000001

for i in range(2, n + 1):
    d[i] = d[i - 1]
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3])
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2])
    d[i] += 1

print(d[n])