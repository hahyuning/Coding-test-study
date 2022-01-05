def op1(l):
    global a
    cnt = 0
    b = [[0] * n for _ in range(n)]
    for sx in range(0, n, l):
        for sy in range(0, n, l):
            ex, ey = sx + l, sy + l

            for i in range(sx, ex):
                for j in range(sy, ey):
                    b[ex - i - 1 + l * cnt][j] = a[i][j]

        cnt += 1
    a = b

def op2(l):
    global a
    cnt = 0
    b = [[0] * n for _ in range(n)]
    for sx in range(0, n, l):
        for sy in range(0, n, l):
            ex, ey = sx + l, sy + l

            for i in range(sx, ex):
                for j in range(sy, ey):
                    b[i][ey - j - 1 + l * cnt] = a[i][j]

            cnt += 1
        cnt = 0
    a = b


def op3(l):
    global a
    cnt = 0
    level = 0
    b = [[0] * n for _ in range(n)]
    for sx in range(0, n, l):
        for sy in range(0, n, l):
            ex, ey = sx + l, sy + l

            for i in range(sx, ex):
                for j in range(sy, ey):
                    b[j - l * level + l * cnt][ex - i - 1 + l * level] = a[i][j]

            level += 1
        cnt += 1
        level = 0
    a = b


def op4(l):
    for _ in range(3):
        op3(l)


def op5(l):
    # 전체 상하반전 후, 부분 상하반전
    op1(n)
    op1(l)


def op6(l):
    op2(n)
    op2(l)


def op7(l):
    # 전체 오른쪽회전 후, 부분 왼쪽회전
    op3(n)
    op4(l)


def op8(l):
    op4(n)
    op3(l)


n, r = map(int, input().split())
n = 2 ** n
a = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r):
    k, l = map(int, input().split())
    l = 2 ** l

    # 1 ~ 4: 배열 내부 - 1: 상하반전, 2: 좌우반전, 3: 오른쪽회전, 4: 왼쪽회전
    if k == 1:
        op1(l)
    elif k == 2:
        op2(l)
    elif k == 3:
        op3(l)
    elif k == 4:
        op4(l)
    # 5 ~ 8: 배열 단위 - 5: 상하반전, 6: 좌우반전, 7: 오른쪽회전, 8: 왼쪽회전
    elif k == 5:
        op5(l)
    elif k == 6:
        op6(l)
    elif k == 7:
        op7(l)
    else:
        op8(l)

for row in a:
    print(*row)
