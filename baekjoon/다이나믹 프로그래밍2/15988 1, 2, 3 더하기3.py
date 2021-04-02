t = int(input())
# d[i] : i를 1, 2, 3의 합으로 나타내는 방법의 수
# d[i] = d[i - 1] + d[i - 2] + d[i - 3]
d = [0] * 1000001
d[0] = 1

for i in range(1, 1000001):
    if i - 1 >= 0:
        d[i] += d[i - 1]
    if i - 2 >= 0:
        d[i] += d[i - 2]
    if i - 3 >= 0:
        d[i] += d[i - 3]
    d[i] %= 1000000009

for _ in range(t):
    n = int(input())
    print(d[n])