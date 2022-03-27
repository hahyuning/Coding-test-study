def solution(money, costs):
    ans = 0
    coins = [1, 5, 10, 50, 100, 500]
    value = []
    for i in range(6):
        value.append((coins[i] / costs[i], coins[i], costs[i]))
    value.sort(reverse=True)

    for val, coin, cost in value:
        n = money // coin
        ans += n * cost
        money -= n * coin

    return ans

solution(1999, [2, 11, 20, 100, 200, 600])