def solution(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 1
    if dist[x][y] != -1:
        return dist[x][y]

    # 탈출 불가로 표시해놓고 시작
    dist[x][y] = 0
    if a[x][y] == "R":
        dist[x][y] = solution(x, y + 1)
    elif a[x][y] == "L":
        dist[x][y] = solution(x, y - 1)
    elif a[x][y] == "U":
        dist[x][y] = solution(x - 1, y)
    else:
        dist[x][y] = solution(x + 1, y)

    return dist[x][y]

n, m = map(int, input().split())
a = [input() for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if dist[i][j] == -1:
            solution(i, j)

ans = 0
for i in range(n):
    for j in range(m):
        if dist[i][j] == 1:
            ans += 1
print(ans)