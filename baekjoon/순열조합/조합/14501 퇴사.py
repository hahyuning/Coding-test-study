n = int(input())
t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

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