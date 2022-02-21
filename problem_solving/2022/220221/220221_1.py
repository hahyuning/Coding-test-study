from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, k = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
check = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0, 0, 0, 1))
check[0][0][0] = True

day = True
ans = -1
while q:
    nq = deque()

    while q:
        x, y, z, cnt = q.popleft()
        if x == n - 1 and y == m - 1:
            ans = cnt
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == "0" and not check[nx][ny][z]:
                    check[nx][ny][z] = True
                    nq.append((nx, ny, z, cnt + 1))
                if z + 1 <= k and board[nx][ny] == "1" and not check[nx][ny][z + 1]:
                    if day:
                        check[nx][ny][z + 1] = True
                        nq.append((nx, ny, z + 1, cnt + 1))
                    else:
                        nq.append((x, y, z, cnt + 1))
    if ans != -1:
        break
    q = nq
    day = not day

print(ans)