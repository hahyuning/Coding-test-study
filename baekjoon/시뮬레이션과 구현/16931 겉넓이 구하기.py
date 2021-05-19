n, m = map(int, input().split())
a = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
a.insert(0, [0] * (m + 2))
a.append([0] * (m + 2))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
for x in range(1, n + 1):
    for y in range(1, m + 1):
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if a[x][y] >= a[nx][ny]:
                answer += (a[x][y] - a[nx][ny])

answer += 2 * m * n
print(answer)
