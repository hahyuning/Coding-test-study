n = int(input())
# d[i] : 3 x i 크기의 벽을 채우는 경우의 수
d = [0] * (n + 1)
d[0] = 1

# 짝수만 가능
for i in range(2, n + 1, 2):
    d[i] = d[i - 2] * 3
    for j in range(i - 4, -1, -2):
        d[i] += d[j] * 2

print(d[n])
