n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# d[i]: 가치의 합이 i원이 되도록 하는 경우의 수
# 마지막에 무엇을 더해서 i원을 만드는지 생각 (오는 곳을 생각하는 방법)
# d[i] = sum(d[i - coins[j]]), 0 <= j <= n
d = [0] * (k + 1)
d[0] = 1

# 중복 없이 세려면 coin 기준으로 계산
for i in range(len(coins)):
    for j in range(1, k + 1):
        if j - coins[i] >= 0:
            d[j] += d[j - coins[i]]

print(d[k])