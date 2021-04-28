n = int(input())
t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액

# dp[i] = i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
# dp[i] = max(p[i] + dp[t[i] + i], maxVal)
dp = [0] * (n + 1)

maxVal = 0
for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n - 1, -1, -1):
    # i 번째 상담을 할 경우 걸리는 시간
    time = t[i] + i

    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # maxVal: i 번째 상담을 하지 않는 경우
        # dp[time] + p[i]: i번째 상담을 하는 경우
        # dp[time]에는 이미 최대 상담 비용이 들어있다.
        dp[i] = max(p[i] + dp[time], maxVal)
        maxVal = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = maxVal

print(maxVal)
