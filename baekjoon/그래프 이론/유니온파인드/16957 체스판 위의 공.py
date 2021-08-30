# 경로 압축 기법
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# (i, j)에서 이동을 마치는 공의 수
check = [0] * (n * m)

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

# (i, j)에서 시작한 공이 이동을 마치는 칸의 번호
parent = [0] * (n * m)

for i in range(n):
    for j in range(m):
        x, y = i, j
        for k in range(8):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] < a[x][y]:
                    x, y = nx, ny

        parent[i * m + j] = x * m + y

for i in range(n):
    for j in range(m):
        check[find(i * m + j)] += 1

for i in range(n):
    for j in range(m):
        print(check[i * m + j], end=" ")
    print()