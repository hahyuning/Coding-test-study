n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    if i != n - 1:
        ans += points[i][0] * points[i + 1][1]
    else:
        ans += points[i][0] * points[0][1]
    ans -= points[i][0] * points[i - 1][1]

ans = abs(ans) / 2
print("{:.1f}".format(ans))