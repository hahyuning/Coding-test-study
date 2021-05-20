# 시간개선 1: 낚시나 이동을 통해 원래 있던 칸에서 상어를 삭제할 때마다 상어 객체를 새로 생성해서 초기화하는게 비효율적
# 상어가 있는지의 여부는 상어의 크기만으로 판단하기 때문에 상어의 크기만 0으로 바꾼다.

# 시간개선 2: 매 이동마다 tmp 배열을 새로 생성하는 것은 비효율적이므로 원래 배열로 복사가 끝나면
# tmp 에 있는 상어의 크기만 0으로 바꾼다.

# 시간개선 3: 상어의 속력이 (움직일 수 있는 곳의 길이) * 2 - 2 보다 큰 경우에는 불필요한 왔다갔다 이동이 생기므로 비효율적
# 속력을 (움직일 수 있는 곳의 길이) * 2 - 2 로 나누었을 때의 나머지로 바꾼다.
class Shark:
    def __init__(self, speed=0, direction=0, size=0):
        self.speed = speed
        self.direction = direction
        self.size = size

n, m, k = map(int, input().split())
# 상어 정보 저장: 기록할 정보가 많기 때문에 객체 사용
shark = [[Shark() for _ in range(m)] for _ in range(n)]
for _ in range(k):
    # 상어의 위치, 속력, 방향, 크기
    r, c, speed, direction, size = map(int, input().split())
    r -= 1
    c -= 1
    direction -= 1

    if direction == 0 or direction == 1:
        speed %= (2 * n - 2)
    elif direction == 2 or direction == 3:
        speed %= (2 * m - 2)
    shark[r][c] = Shark(speed, direction, size)

# 위 아래 오른쪽 왼쪽
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 2. 상어 이동 -> 이동한 후의 위치, 방향 반환
# 상어가 이동하다가 벽을 만나면 방향을 반대로 바꿈
def move(a, b, speed, direction):
    for k in range(speed):
        # 벽에 부딪히는 경우 처리
        if direction == 0:
            if a == 0:
                a = 1
                direction = 1
            else:
                a -= 1
        elif direction == 1:
            if a == n - 1:
                a = n - 2
                direction = 0
            else:
                a += 1
        elif direction == 2:
            if b == m - 1:
                b = m - 2
                direction = 3
            else:
                b += 1
        elif direction == 3:
            if b == 0:
                b = 1
                direction = 2
            else:
                b -= 1
    return (a, b, direction)

# 1. 낚시왕 이동

# 상어의 이동 기록을 위한 임시 리스트
tmp = [[Shark() for _ in range(m)] for _ in range(n)]
ans = 0
for j in range(m):
    for i in range(n):
        # 상어를 잡은 경우 (상어의 크기가 존재하면 상어 존재)
        if shark[i][j].size > 0:
            ans += shark[i][j].size
            shark[i][j].size = 0
            break

    # 2. 상어 이동
    for a in range(n):
        for b in range(m):
            if shark[a][b].size != 0:
                now = shark[a][b]
                x, y, d = move(a, b, now.speed, now.direction)
                # 이동한 칸에 상어가 없거나
                # 이동한 칸에 있는 상어의 크기가 현재 상어보다 작은 경우
                if tmp[x][y].size == 0 or tmp[x][y].size < now.size:
                    tmp[x][y] = Shark(now.speed, d, now.size)

    # 동시 이동 처리
    for a in range(n):
        for b in range(m):
            shark[a][b] = Shark(tmp[a][b].speed, tmp[a][b].direction, tmp[a][b].size)
            tmp[a][b].size = 0
print(ans)