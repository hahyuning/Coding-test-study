n = int(input())
a = [list(input()) for _ in range(n)]
c = [[-1] * n for _ in range(n)]
ans = 0

dx = [-1, -1, 0, 0, 1, 1]
dy = [0, 1, -1, 1, -1, 0]

def dfs(x, y, color):
    global ans
    c[x][y] = color

    # 색칠해야 하므로 정답이 0이 아님
    ans = max(ans, 1)

    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == "X":

                # 인접한 칸을 아직 방문하지 않은 경우
                if c[nx][ny] == -1:
                    dfs(nx, ny, 1 - color)

                # 인접한 칸이 존재하므로 정답이 1이 아님
                ans = max(ans, 2)

                # 인접한 칸을 이미 방문한 경우
                if c[nx][ny] == color:
                    # 색을 하나 더 사용
                    ans = max(ans, 3)

for i in range(n):
    for j in range(n):
        if a[i][j] == 'X' and c[i][j] == -1:
            dfs(i, j, 0)

print(ans)