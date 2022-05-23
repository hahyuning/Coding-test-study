from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_block():
    # 그룹에는 일반 블록이 적어도 하나, 일반 블록의 색은 모두 같아야 한다.
    # 검은색 블록은 포함되면 안되고, 무지개 블록은 얼마나 있던 상관 x
    # 그룹에 속한 블록 개수는 2보다 크거나 같아야 한다.
    # 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록

    # (블록 사이즈, 기준 블록 좌표)
    block_info = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] <= 0:
                continue

            if not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True

                color = a[i][j]
                size = 0
                sx, sy = i, j
                rainbow = []
                while q:
                    x, y = q.popleft()
                    size += 1

                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            if a[nx][ny] in [color, 0]:
                                visited[nx][ny] = True
                                q.append((nx, ny))

                                if a[nx][ny] == 0:
                                    rainbow.append((nx, ny))

                for x, y in rainbow:
                    visited[x][y] = False
                if size >= 2:
                    block_info.append((size, len(rainbow), sx, sy))

    return block_info

def remove_block(x, y):
    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    color = a[x][y]

    while q:
        x, y = q.popleft()
        a[x][y] = -2

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if a[nx][ny] in [color, 0]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

def move_block():
    for j in range(n):
        for i in range(n - 2, -1, -1):
            if a[i][j] >= 0:
                max_row = i
                for k in range(i + 1, n):
                    if a[k][j] == -2:
                        max_row = k
                    else:
                        break

                if max_row != i:
                    a[i][j], a[max_row][j] = -2, a[i][j]

def rotate_board():
    b = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            b[i][j] = a[j][n - i - 1]

    return b


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    while True:
        block_info = find_block()
        if not block_info:
            break

        block_info.sort(key=lambda x:(x[0], x[1], x[2], x[3]), reverse=True)
        x, y = block_info[0][2], block_info[0][3]
        remove_block(x, y)
        ans += block_info[0][0] ** 2

        move_block()
        a = rotate_board()
        move_block()

    print(ans)



