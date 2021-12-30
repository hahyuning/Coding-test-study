from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 1. 가장 가까운 승객 찾기
def find_guest(sx, sy):
    # 택시가 있는 위치에 손님이 있는 경우
    if (sx, sy) in guest:
        return (sx, sy, 0)

    q = deque()
    q.append((sx, sy))
    check = [[-1] * n for _ in range(n)]
    check[sx][sy] = 0
    res = []

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == -1 and a[nx][ny] != 1:
                if (nx, ny) in guest:
                    res.append((nx, ny, check[x][y] + 1))
                q.append((nx, ny))
                check[nx][ny] = check[x][y] + 1
    if not res:
        return (-1, -1, -1)
    else:
        res.sort(key=lambda x:(x[2], x[0], x[1]))
        return (res[0][0], res[0][1], res[0][2])

# 손님이 이동할 거리 구하기
def find_guest_dist(sx, sy):
    q = deque()
    q.append((sx, sy))
    check = [[-1] * n for _ in range(n)]
    check[sx][sy] = 0

    ex, ey = guest[(sx, sy)]

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == -1 and a[nx][ny] != 1:
                if (nx, ny) == (ex, ey):
                    return check[x][y] + 1
                else:
                    q.append((nx, ny))
                    check[nx][ny] = check[x][y] + 1

    # 승객이 도착지에 갈 수 없는 경우
    return -1

n, m, fuel = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
sx, sy = map(int, input().split())
sx -= 1
sy -= 1
guest = dict()
for _ in range(m):
    x, y, w, z = map(int, input().split())
    x -= 1
    y -= 1
    w -= 1
    z -= 1
    guest[(x, y)] = (w, z)

flg = True
while True:
    gx, gy, d = find_guest(sx, sy)
    if d == -1:
        if len(guest.keys()) != 0:
            flg = False
        break

    if d <= fuel:
        fuel -= d
        use = find_guest_dist(gx, gy)
        if use == -1:
            flg = False
            break

        if use <= fuel:
            fuel += find_guest_dist(gx, gy)
            sx, sy = guest[(gx, gy)]
            del guest[(gx, gy)]
        else:
            flg = False
            break
    else:
        flg = False
        break

print(fuel if flg else -1)
