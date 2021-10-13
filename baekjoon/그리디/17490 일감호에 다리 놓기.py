import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
cost = list(map(int, input().split()))

tmp = []
for _ in range(m):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if a == 1 and b == n:
        tmp.append((b - 1, a - 1))
    else:
        tmp.append((a - 1, b - 1))
tmp.sort()

if m <= 1:
    print("YES")
else:
    ans = 0
    last = 0

    for x, y in tmp:
        min_cost = 1000000
        for i in range(last, x + 1):
            min_cost = min(min_cost, cost[i])

        if last == 0 and tmp[-1][1] != 0:
            end = tmp[-1][1]
            for i in range(end, n):
                min_cost = min(min_cost, cost[i])

        ans += min_cost
        last = y

    if ans > k:
        print("NO")
    else:
        print("YES")
