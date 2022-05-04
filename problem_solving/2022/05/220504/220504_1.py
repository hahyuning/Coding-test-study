from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    dist = [[0] * n for _ in range(n)]
    q = deque()
    q.append((sx, sy, h, 0, 0))
    dist[sx][sy] = h

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y, now_h, now_d, cnt = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == "E":
                    print(cnt + 1)
                    return

                nxt_h, nxt_d = now_h, now_d
                if a[nx][ny] == "U":
                    nxt_d = d

                if nxt_d > 0:
                    nxt_d -= 1
                else:
                    nxt_h -= 1

                if nxt_h > 0 and dist[nx][ny] < nxt_h:
                    dist[nx][ny] = nxt_h
                    q.append((nx, ny, nxt_h, nxt_d, cnt + 1))

    print(-1)


if __name__ == '__main__':
    n, h, d = map(int, input().split())
    a = [input().rstrip() for _ in range(n)]

    sx, sy = -1, -1
    for i in range(n):
        for j in range(n):
            if a[i][j] == "S":
                sx, sy = i, j
    bfs()