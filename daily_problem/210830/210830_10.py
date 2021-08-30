n = int(input())
l = list(map(int, input().split()))
cost = list(map(int, input().split()))

ans = l[0] * cost[0]
now = cost[0]
dist = 0
for i in range(1, n - 1):
    if cost[i] < now:
        # 이전까지의 계산 결과 더하기
        ans += now * dist
        # 새로운 가격으로 갱신
        now = cost[i]
        dist = l[i]
    else:
        dist += l[i]

# 마지막 도시 처리
ans += now * dist
print(ans)