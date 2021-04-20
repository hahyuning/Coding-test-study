n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# d[i]: 가치의 합이 i원이 되도록 하는 경우의 수
d = [0] * (k + 1)
d[0] = 1

for i in range(n):
    for j in range(1, k + 1):
        if j - coins[i] >= 0:
            d[j] += d[j - coins[i]]

print(d[k])