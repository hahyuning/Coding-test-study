# dp[i] = i번째 날부터 마지막 날가지 낼 수 있는 최대 이익
# dp[i] = max(p[i] + dp[t[i] + i], maxVal)

n = int(input())
t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
# dp = [0] * (n + 1)
# maxVal = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# for i in range(n - 1, -1, -1):
#     time = t[i] + i
#
#     # 상담이 기간 안에 끝나는 경우
#     if time <= n:
#         dp[i] = max(p[i] + dp[t[i] + i], maxVal)
#         maxVal = dp[i]
#     # 상담이 기간을 벗어나는 경우
#     else:
#         dp[i] = maxVal
#
# print(maxVal)

answer = 0

def combination(day, sum):
    global answer

    if day == n:
        answer = max(answer, sum)
        return
    if day > n:
        return

    combination(day + 1, sum)
    combination(day + t[day], sum + p[day])

combination(0, 0)
print(answer)