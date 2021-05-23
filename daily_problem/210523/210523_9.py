t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    d = [0] * (target + 1)
    d[0] = 1

    for coin in coins:
        for price in range(target + 1):
            if price - coin >= 0:
                d[price] += d[price - coin]
    print(d[target])