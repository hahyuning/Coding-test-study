def move_sand(x, y, dir, a):
    global ans
    if dir == 0 or dir == 2:
        if 0 <= y + 2 * dy[dir] < n:
            a[x][y + 2 * dy[dir]] += int(a[x][y] * 0.05)
        else:
            ans += int(a[x][y] * 0.05)

        if 0 <= y + dy[dir] < n and 0 <= x + dy[dir] < n:
            a[x + dy[dir]][y + dy[dir]] += int(a[x][y] * 0.1)
        else:
            ans += int(a[x][y] * 0.1)

        if 0 <= y + dy[dir] < n and 0 <= x - dy[dir] < n:
            a[x - dy[dir]][y + dy[dir]] += int(a[x][y] * 0.1)
        else:
            ans += int(a[x][y] * 0.1)

        if 0 <= x - dy[dir] < n:
            a[x - dy[dir]][y] += int(a[x][y] * 0.07)
        else:
            ans += int(a[x][y] * 0.07)

        if 0 <= x + dy[dir] < n:
            a[x + dy[dir]][y] += int(a[x][y] * 0.07)
        else:
            ans += int(a[x][y] * 0.07)

        if 0 <= x - 2 * dy[dir] < n:
            a[x - 2 * dy[dir]][y] += int(a[x][y] * 0.02)
        else:
            ans += int(a[x][y] * 0.02)

        if 0 <= x + 2 * dy[dir] < n:
            a[x + 2 * dy[dir]][y] += int(a[x][y] * 0.02)
        else:
            ans += int(a[x][y] * 0.02)

        if 0 <= x + dy[dir] < n and 0 <= y - dy[dir] < n:
            a[x + dy[dir]][y - dy[dir]] += int(a[x][y] * 0.02)
        else:
            ans += int(a[x][y] * 0.01)

        if 0 <= x - dy[dir] < n and 0 <= y - dy[dir] < n:
            a[x - dy[dir]][y - dy[dir]] += int(a[x][y] * 0.01)
        else:
            ans += int(a[x][y] * 0.01)

        if 0 <= y + dy[dir] < n:
            a[x][y + dy[dir]] = a[x][y] * 0.55
        else:
            ans += a[x][y] * 0.55

        a[x][y] = 0

    else:
        if 0 <= x + 2 * dx[dir] < n:
            a[x + 2 * dx[dir]][y] += int(a[x][y] * 0.05)
        else:
            ans += int(a[x][y] * 0.05)

        if 0 <= y + dx[dir] < n and 0 <= x + dx[dir] < n:
            a[x + dx[dir]][y + dy[dir]] += int(a[x][y] * 0.1)
        else:
            ans += int(a[x][y] * 0.1)

        if 0 <= x + dx[dir] < n and 0 <= y - dx[dir] < n:
            a[x + dx[dir]][y - dx[dir]] += int(a[x][y] * 0.1)
        else:
            ans += int(a[x][y] * 0.1)

        if 0 <= y - dx[dir] < n:
            a[x][y - dx[dir]] += int(a[x][y] * 0.07)
        else:
            ans += int(a[x][y] * 0.07)

        if 0 <= y + dx[dir] < n:
            a[x][y + dx[dir]] += int(a[x][y] * 0.07)
        else:
            ans += int(a[x][y] * 0.07)

        if 0 <= y - 2 * dx[dir] < n:
            a[x][y - 2 * dx[dir]] += int(a[x][y] * 0.02)
        else:
            ans += int(a[x][y] * 0.02)

        if 0 <= y + 2 * dx[dir] < n:
            a[x][y + 2 * dx[dir]] += int(a[x][y] * 0.02)
        else:
            ans += int(a[x][y] * 0.02)

        if 0 <= y + dx[dir] < n and 0 <= x - dx[dir] < n:
            a[x - dx[dir]][y + dx[dir]] += int(a[x][y] * 0.02)
        else:
            ans += int(a[x][y] * 0.01)

        if 0 <= x - dx[dir] < n and 0 <= y - dx[dir] < n:
            a[x - dx[dir]][y - dx[dir]] += int(a[x][y] * 0.01)
        else:
            ans += int(a[x][y] * 0.01)

        if 0 <= x + dx[dir] < n:
            a[x + dx[dir]][y] = a[x][y] * 0.55
        else:
            ans += a[x][y] * 0.55

        a[x][y] = 0

    return a

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = n // 2
ans = 0

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

x, y = m, m
move = 1
cnt = 0
dir = 0
while True:
    if x == 0 and y == 0:
        break

    for _ in range(move):
        nx, ny = x + dx[dir], y + dy[dir]
        a = move_sand(nx, ny, dir, a)

        x, y = nx, ny
        if x == 0 and y == 0:
            break

    cnt += 1
    dir = (dir + 1) % 4
    if cnt == 2:
        move += 1
        cnt = 0

print(ans)