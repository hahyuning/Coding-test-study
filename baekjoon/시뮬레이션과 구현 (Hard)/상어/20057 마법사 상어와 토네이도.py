class Wind:
    def __init__(self, dx, dy, ratio):
        self.dx = dx
        self.dy = dy
        self.ratio = ratio


# 서남독북
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# 흩날리는 먼지 정보 회전
def rotation(x):
    res = []
    for w in x:
        nx = -w.dy
        ny = w.dx
        res.append(Wind(nx, ny, w.ratio))
    return res


# i 방향에서 흩날리는 먼지 정보 저장
d = []
tmp = []
tmp.append(Wind(0, -2, 5))
tmp.append(Wind(-1, -1, 10))
tmp.append(Wind(1, -1, 10))
tmp.append(Wind(-1, 0, 7))
tmp.append(Wind(-2, 0, 2))
tmp.append(Wind(1, 0, 7))
tmp.append(Wind(2, 0, 2))
tmp.append(Wind(-1, 1, 1))
tmp.append(Wind(1, 1, 1))
d.append(tmp)

for _ in range(3):
    tmp = rotation(tmp)
    d.append(tmp)

# 입력
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * n for _ in range(n)]

x = (n - 1) // 2
y = (n - 1) // 2
# 회전 체크용 배열
check[x][y] = True

dir = 0
ans = 0
while True:
    # 모래 이동
    nx = x + dx[dir]
    ny = y + dy[dir]
    check[nx][ny] = True

    sand = a[nx][ny]
    a[nx][ny] = 0
    x, y = nx, ny

    # 모래 흩날리기
    used = 0  # 흩날린 모래의 양
    for w in d[dir]:
        nx = x + w.dx
        ny = y + w.dy
        tmp = sand * w.ratio // 100
        used += tmp

        if 0 <= nx < n and 0 <= ny < n:
            a[nx][ny] += tmp
        else:
            ans += tmp

    # 알파 처리
    sand -= used
    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0 <= nx < n and 0 <= ny < n:
        a[nx][ny] += sand
    else:
        ans += sand

    # 종료조건
    if x == 0 and y == 0:
        break

    # 진행 방향 회전 여부 확인
    ndir = (dir + 1) % 4
    nx = x + dx[ndir]
    ny = y + dy[ndir]
    if not check[nx][ny]:
        dir = ndir

print(ans)
