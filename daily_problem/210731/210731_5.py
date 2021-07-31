coins = list(map(int, input().split()))
amount = int(input())

d = [-1] * (amount + 1)
d[0] = 0

for i in range(len(coins)):
    for j in range(1, amount + 1):
        if j - coins[i] >= 0 and d[j - coins[i]] != -1:
            if d[j] == -1 or d[j] > d[j - coins[i]] + 1:
                d[j] = d[j - coins[i]] + 1

print(d[amount])