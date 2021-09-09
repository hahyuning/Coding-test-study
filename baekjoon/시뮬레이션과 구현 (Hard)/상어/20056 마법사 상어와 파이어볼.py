class Shark():
    def __init__(self, mess=0, speed=0, dir=0):
        self.mess = mess
        self.speed = speed
        self.dir = dir

d = {0:[-1, 0], 1:[-1, 1], 2:[0, 1], 3:[1, 1], 4:[1, 0], 5:[1, -1], 6:[0, -1], 7:[-1, -1]}

n, m, k = map(int, input().split())
shark = dict()
for _ in range(m):
    r, c, mess, speed, dir = map(int, input().split())
    r -= 1
    c -= 1
    if (r, c) not in shark:
        shark[(r, c)] = [Shark(mess, speed, dir)]
    else:
        shark[(r, c)].append(Shark(mess, speed, dir))

for _ in range(k):
    tmp_mess = [[0] * n for _ in range(n)]
    tmp_speed = [[0] * n for _ in range(n)]
    tmp_cnt = [[0] * n for _ in range(n)]
    tmp_shark = dict()
    # 상어 이동
    for i in range(n):
        for j in range(n):
            if (i, j) in shark:
                for s in shark[(i, j)]:
                    sp = s.speed % n
                    nx, ny = i + d[s.dir][0] * sp, j + d[s.dir][1] * sp
                    if nx < 0:
                        nx += n
                    if ny < 0:
                        ny += n
                    if nx >= n:
                        nx -= n
                    if ny >= n:
                        ny -= n
                    if (nx, ny) not in tmp_shark:
                        tmp_shark[(nx, ny)] = [Shark(s.mess, s.speed, s.dir)]
                    else:
                        tmp_shark[(nx, ny)].append(Shark(s.mess, s.speed, s.dir))
                    tmp_mess[nx][ny] += s.mess
                    tmp_speed[nx][ny] += s.speed
                    tmp_cnt[nx][ny] += 1

    tmp_dir = [[True] * n for _ in range(n)]
    for x in tmp_shark:
        check = True
        dir = tmp_shark[x][0].dir
        for s in tmp_shark[x]:
            if dir % 2 != s.dir % 2:
                check = False
        tmp_dir[x[0]][x[1]] = check

    for i in range(n):
        for j in range(n):
            if tmp_cnt[i][j] >= 2 and tmp_mess[i][j] != 0:
                mess = tmp_mess[i][j] // 5
                speed = tmp_speed[i][j] // tmp_cnt[i][j]

                if mess == 0:
                    tmp_shark[(i, j)] = []
                    continue

                s = []
                if tmp_dir[i][j]:
                    for k in range(0, 7, 2):
                        s.append(Shark(mess, speed, k))
                else:
                    for k in range(1, 8, 2):
                        s.append(Shark(mess, speed, k))
                tmp_shark[(i, j)] = s
    shark = tmp_shark

ans = 0
for y in shark.values():
    for x in y:
        ans += x.mess
print(ans)