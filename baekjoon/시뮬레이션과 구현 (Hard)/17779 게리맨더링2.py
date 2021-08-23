from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 2. 각 영역 채우기
def bfs(b, x, y, num):
    b[x][y] = num
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if b[nx][ny] == 0:
                    b[nx][ny] = num
                    q.append((nx, ny))

# 1. 자치구 경계 설정
def solution(x, y, d1, d2):
    b = [[0] * n for _ in range(n)]

    # 5번 자치구 경계
    for i in range(d1 + 1):
        b[x + i][y - i] = 5
        b[x + d2 + i][y + d2 - i] = 5
    for i in range(d2 + 1):
        b[x + i][y + i] = 5
        b[x + d1 + i][y - d1 + i] = 5

    # 3번 자치구 경계
    for j in range(y - d1):
        b[x + d1][j] = 3
    # 1번 자치구 경계
    for i in range(x):
        b[i][y] = 1
    # 2번 자치구 경계
    for j in range(y + d2 + 1, n):
        b[x + d2][j] = 2
    # 4번 자치구 경계
    for i in range(x + d1 + d2 + 1, n):
        b[i][y - d1 + d2] = 4

    bfs(b, 0, 0, 1)
    bfs(b, 0, n - 1, 2)
    bfs(b, n - 1, 0, 3)
    bfs(b, n - 1, n - 1, 4)

    # 3. 각 영역의 넓이 구하기
    cnt = [0] * 6
    for i in range(n):
        for j in range(n):
            if b[i][j] == 0:
                b[i][j] = 5

            cnt[b[i][j]] += a[i][j]

    cnt = cnt[1:]
    cnt.sort()
    ans = cnt[-1] - cnt[0]
    return ans

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ans = -1
for x in range(n):
    for y in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                # 열 검사
                if 0 <= y - d1 and y + d2 < n:
                    # 행 검사
                    if x + d1 + d2 < n:
                        tmp = solution(x, y, d1, d2)
                        if ans == -1 or tmp < ans:
                            ans = tmp
print(ans)