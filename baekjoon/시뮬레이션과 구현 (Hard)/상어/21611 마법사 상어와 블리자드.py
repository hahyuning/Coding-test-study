def make_line(a):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    b = []
    x, y = n // 2, n // 2
    k = 1
    l = 0
    dir = 3

    while True:
        if x < -1 or x >= n or y < -1 or y >= n:
            break

        for _ in range(k):
            x, y = x + dx[dir], y + dy[dir]
            if x < -1 or x >= n or y < -1 or y >= n:
                break
            if 0 <= x < n and 0 <= y < n and a[x][y] != 0:
                b.append(a[x][y])
        l += 1
        if l == 2:
            k += 1
            l = 0
        dir = (dir + 1) % 4
    return b

def bomb(b):
    global ans

    ball_cnt = [0] * 4
    e = []

    # 폭발이 더이상 일어나지 않을 때까지 반복
    while True:
        flg = False
        # 각 구슬이 몇번 나오는지 기록
        c = []
        i = 0
        while i < len(b):
            if b[i] == 0:
                i += 1
                continue

            cnt = 0
            for j in range(i, len(b)):
                if b[i] == b[j]:
                    cnt += 1
                else:
                    break
            c.append((b[i], cnt))
            i += cnt

        b = []
        for x, y in c:
            if x == 0:
                continue

            if y >= 4:
                ball_cnt[x] += y
                flg = True
            else:
                for _ in range(y):
                    b.append(x)

        if flg == False:
            e = c
            break

    f = []
    for x, y in e:
        f.append(y)
        f.append(x)

    if len(f) > n ** 2 - 1:
        f = f[:n ** 2 - 1]

    for i in range(4):
        ans += i * ball_cnt[i]

    return f

def make_map(b):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    a = [[0] * n for _ in range(n)]
    x, y = n // 2, n // 2
    k = 1
    l = 0
    dir = 3
    pnt = 0

    while pnt < len(b):
        for _ in range(k):
            x, y = x + dx[dir], y + dy[dir]
            if pnt >= len(b):
                break

            a[x][y] = b[pnt]
            pnt += 1

        l += 1
        if l == 2:
            k += 1
            l = 0
        dir = (dir + 1) % 4
    return a

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
command = [list(map(int, input().split())) for _ in range(m)]

dir = {1:[-1, 0], 2:[1, 0], 3:[0, -1], 4: [0, 1]}

ans = 0
for i in range(m):
    d, s = command[i]
    x, y = n // 2, n // 2
    cnt = 0
    while cnt < s:
        x, y = x + dir[d][0], y + dir[d][1]
        a[x][y] = 0
        cnt += 1

    b = make_line(a)
    b = bomb(b)
    a = make_map(b)

print(ans)