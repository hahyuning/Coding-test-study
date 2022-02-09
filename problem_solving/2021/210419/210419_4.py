n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# d[i]: 가치의 합이 i원이 되도록 하는 최소 개수
d = [-1] * (k + 1)
d[0] = 0

for i in range(len(coins)):
    for j in range(1, k + 1):
        if j - coins[i] >= 0 and d[j - coins[i]] != -1:
            if d[j] == -1 or d[j] > d[j - coins[i]] + 1:
                d[j] = d[j - coins[i]] + 1

print(d[k])