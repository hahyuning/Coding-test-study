from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    # 칸을 검사했는지 체크
    check = [[False] * n for _ in range(n)]
    # 인구 이동이 일어나는지 체크
    move = False

    for i in range(n):
        for j in range(n):
            if check[i][j] == False:
                q = deque()
                q.append((i, j))
                check[i][j] = True

                # 연합을 이루는 칸의 좌표 저장
                stack = [(i, j)]
                # 연합을 이루는 칸의 총 인구
                total = a[i][j]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == False:
                            # 인구의 차이
                            diff = abs(a[x][y] - a[nx][ny])
                            if l <= diff <= r:
                                q.append((nx, ny))
                                stack.append((nx, ny))
                                check[nx][ny] = True
                                move = True
                                total += a[nx][ny]

                val = total // len(stack)
                for x, y in stack:
                    a[x][y] = val
    return move

n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
while True:
    if bfs():
        ans += 1
    else:
        break
print(ans)
