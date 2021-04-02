t = int(input())
# d[n] = n을 1, 2, 3의 합으로 나타내는 방법의 수
# d[n] = d[n - 1] + d[n - 2] + d[n - 3]
d = [0] * 11
d[0] = 1
d[1] = 1
d[2] = 2

for i in range(3, 11):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]

for _ in range(t):
    n = int(input())
    print(d[n])
