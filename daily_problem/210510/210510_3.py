cube = [["0010", "1111", "0010"],
    ["0100", "1111", "1000"],
    ["0010", "1111", "0100"],
    ["0001", "1111", "1000"],
    ["0001", "1111", "0100"],
    ["11100", "00111"],
    ["1100", "0111", "0010"],
    ["1100", "0111", "0001"],
    ["0010", "1110", "0011"],
    ["0001", "1111", "0001"],
    ["1100", "0110", "0011"]]

def check(b):
    n = len(b)
    c = []
    for i in range(n):
        c.append("".join(map(str, b[i])))

    if c in cube:
        return True
    return False

# 90도 회전
def rotate(b):
    n = len(b)
    m = len(b[0])
    res = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            res[j][i] = b[i][j]
    return res

# 좌우 반전
def mirror_1(b):
    n = len(b)
    m = len(b[0])
    res = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            res[i][j] = b[i][m - j - 1]
    return res

# 상하 반전
def mirror_2(b):
    n = len(b)
    m = len(b[0])
    res = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            res[i][j] = b[n - i - 1][j]
    return res

for _ in range(3):
    a = [list(map(int, input().split())) for _ in range(6)]
    # 4 x 3
    ch = False
    for i in range(0, 3):
        for j in range(0, 4):
            b = [[0] * 3 for _ in range(4)]
            for k in range(4):
                for l in range(3):
                    b[k][l] = a[i + k][j + l]

            b = rotate(b)
            if check(b):
                ch = True
            b = mirror_1(b)
            if check(b):
                ch = True

            b = mirror_2(b)
            if check(b):
                ch = True
            b = mirror_1(b)
            if check(b):
                ch = True

    # 3 x 4
    for i in range(0, 4):
        for j in range(0, 3):
            b = [[0] * 4 for _ in range(3)]
            for k in range(3):
                for l in range(4):
                    b[k][l] = a[i + k][j + l]

            if check(b):
                ch = True
            b = mirror_1(b)
            if check(b):
                ch = True

            b = mirror_2(b)
            if check(b):
                ch = True
            b = mirror_1(b)
            if check(b):
                ch = True

    # 2 X 5
    for i in range(0, 5):
        for j in range(0, 2):
            b = [[0] * 5 for _ in range(2)]
            for k in range(2):
                for l in range(5):
                    b[k][l] = a[i + k][j + l]

            if check(b):
                ch = True
            b = mirror_1(b)
            if check(b):
                ch = True

            b = mirror_2(b)
            if check(b):
                ch = True
            b = mirror_1(b)
            if check(b):
                ch = True

    # 5 X 2
    for i in range(0, 2):
        for j in range(0, 5):
            b = [[0] * 2 for _ in range(5)]
            for k in range(5):
                for l in range(2):
                    b[k][l] = a[i + k][j + l]

            b = rotate(b)
            if check(b):
                ch = True
            b = mirror_1(b)
            if check(b):
                ch = True

            b = mirror_2(b)
            if check(b):
                ch = True
            b = mirror_1(b)
            if check(b):
                ch = True

    if ch == True:
        print("yes")
    else:
        print("no")
