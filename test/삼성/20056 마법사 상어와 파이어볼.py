from collections import defaultdict

class Shark:
    def __init__(self, mess=0, speed=0, dir=0):
        self.mess = mess
        self.speed = speed
        self.dir = dir

d = {0:[-1, 0], 1:[-1, 1], 2:[0, 1], 3:[1, 1], 4:[1, 0], 5:[1, -1], 6:[0, -1], 7:[-1, -1]}

n, m, k = map(int, input().split())

# 파이어볼의 정보 저장
shark = defaultdict(list)
for _ in range(m):
    r, c, mess, speed, dir = map(int, input().split())
    r -= 1
    c -= 1

    shark[(r, c)].append(Shark(mess, speed, dir))

for _ in range(k):
    tmp_shark = defaultdict(list)
    # 상어 이동
    for i in range(n):
        for j in range(n):
            if (i, j) in shark:
                for s in shark[(i, j)]:
                    sp = s.speed % n
                    nx, ny = i + d[s.dir][0] * sp, j + d[s.dir][1] * sp
                    nx, ny = (nx % n + n) % n, (ny % n + n) % n

                    tmp_shark[(nx, ny)].append(Shark(s.mess, s.speed, s.dir))
    shark = tmp_shark

    # 정보 갱신
    for i in range(n):
        for j in range(n):
            if len(shark[(i, j)]) > 0:
                total_m = 0
                total_s = 0
                cnt = len(shark[(i, j)])

                standard_d = shark[(i, j)][0].dir % 2
                result_d = 0

                for s in shark[(i, j)]:
                    if s.dir % 2 != standard_d:
                        result_d = 1

                    total_m += s.mess
                    total_s += s.speed

                shark[(i, j)].clear()

                shark_m = total_m // 5
                shark_s = total_s // cnt
                if shark_m > 0:
                    for direction in range(4):
                        shark[(i, j)].append(Shark(shark_m, shark_s, direction * 2 + result_d))

ans = 0
for y in shark.values():
    for x in y:
        ans += x.mess
print(ans)