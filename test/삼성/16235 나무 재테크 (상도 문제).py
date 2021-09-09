n, m, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)] # 겨울에 더해질 양분 정보
yangbun = [[5] * n for _ in range(n)] # 각 칸의 양분 정보
tree = [[[] for _ in range(n)] for _ in range(n)] # 각 칸에 위치한 나무들의 나이
for _ in range(m):
    x, y, age = map(int, input().split())
    tree[x - 1][y - 1].append(age)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# l년이 지난 후 살아남은 나무의 개수 구하기
for _ in range(l):
    # 각 칸마다 봄, 여름, 가을, 겨울 순차적으로 진행
    # 동시에 번식하는 가을은 따로 처리 필요
    fall = [[0] * n for _ in range(n)] # 가을에 추가되어야 하는 나이가 1인 나무의 개수

    for i in range(n):
        for j in range(n):
            # ----------봄----------
            tree[i][j].sort()
            aged = [] # 나이가 증가한 나무들의 나이
            dead = 0 # 여름에 양분으로 변할 죽은 나무들의 나이
            for t in tree[i][j]:
                # 나무가 자신의 나이만큼 나이를 먹고, 나이 1 증가
                if t <= yangbun[i][j]:
                    yangbun[i][j] -= t
                    aged.append(t + 1)

                    # ----------가을----------
                    if (t + 1) % 5 == 0:
                        for k in range(8):
                            nx, ny = i + dx[k], j + dy[k]
                            if 0 <= nx < n and 0 <= ny < n:
                                fall[nx][ny] += 1
                else:
                    dead += t // 2

            tree[i][j] = aged

            # ----------여름----------
            yangbun[i][j] += dead
            # ----------겨울----------
            yangbun[i][j] += a[i][j]

    # ----------가을----------
    for i in range(n):
        for j in range(n):
            for k in range(fall[i][j]):
                tree[i][j].append(1)

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])
print(ans)
