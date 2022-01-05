def operation1(a):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = a[n - i - 1][j]
    return ans


def operation5(a, l):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    sub_size = (1 << l)
    sub_count = n // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = (sub_count - i - 1) * sub_size
            y2 = j * sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1 + x][y1 + y] = a[x2 + x][y2 + y]
    return ans


def operation2(a):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = a[i][n - j - 1]
    return ans


def operation6(a, l):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    sub_size = (1 << l)
    sub_count = n // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = i * sub_size
            y2 = (sub_count - j - 1) * sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1 + x][y1 + y] = a[x2 + x][y2 + y]
    return ans


def operation3(a):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = a[n - j - 1][i]
    return ans


def operation7(a, l):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    sub_size = (1 << l)
    sub_count = n // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = (sub_count - j - 1) * sub_size
            y2 = i * sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1 + x][y1 + y] = a[x2 + x][y2 + y]
    return ans


def operation4(a):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = a[j][n - i - 1]
    return ans


def operation8(a, l):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    sub_size = (1 << l)
    sub_count = n // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = j * sub_size
            y2 = (sub_count - i - 1) * sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1 + x][y1 + y] = a[x2 + x][y2 + y]
    return ans


def operation_1_to_4(a, k, sx, sy, length):
    b = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            b[i][j] = a[sx + i][sy + j]

    if k == 1:
        b = operation1(b)
    elif k == 2:
        b = operation2(b)
    elif k == 3:
        b = operation3(b)
    elif k == 4:
        b = operation4(b)

    for i in range(length):
        for j in range(length):
            a[sx + i][sy + j] = b[i][j]


n, r = map(int, input().split())
size = (1 << n)
a = [list(map(int, input().split())) for _ in range(size)]

for _ in range(r):
    k, l = map(int, input().split())
    sub_size = (1 << l)
    if 1 <= k <= 4:
        for i in range(0, size, sub_size):
            for j in range(0, size, sub_size):
                operation_1_to_4(a, k, i, j, sub_size)
    elif 5 <= k <= 8:
        if k == 5:
            a = operation5(a, l)
        elif k == 6:
            a = operation6(a, l)
        elif k == 7:
            a = operation7(a, l)
        elif k == 8:
            a = operation8(a, l)

for i in range(size):
    print(' '.join(map(str, a[i])))


# -----------------------------------------------------------------------------------
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
