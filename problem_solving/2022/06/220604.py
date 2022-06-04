n = int(input())
points = [[] for _ in range(n + 1)]
for _ in range(n):
    x, y = map(int, input().split())
    points[y].append(x)

ans = 0
for i in range(n + 1):
    if len(points[i]) > 1:
        points[i].sort()
        for j in range(len(points[i])):
            if j == 0:
                ans += points[i][j + 1] - points[i][j]
            elif j == len(points[i]) - 1:
                ans += points[i][j] - points[i][j - 1]
            else:
                ans += min(points[i][j + 1] - points[i][j], points[i][j] - points[i][j - 1])

print(ans)