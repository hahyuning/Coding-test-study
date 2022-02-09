n = int(input())
check = [True] * (n + 1)
coins = []
for i in range(2, n + 1):
    if check[i]:
        coins.append(i)
        for j in range(2 * i, n + 1, i):
            check[j] = False

d = [0] * (n + 1)
d[0] = 1
for i in range(len(coins)):
    for j in range(coins[i], n + 1):
        d[j] += d[j - coins[i]]
        d[j] %= 123456789

print(d[n])