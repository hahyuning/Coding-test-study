import sys

def omok(x, y):
    c1 = True
    # 세로 검사
    if y + 4 <= 18:
        for i in range(1, 5):
            if a[x][y] != a[x][y + i]:
                c1 = False
                break
        else:
            if y + 5 <= 18 and a[x][y] == a[x][y + 5]:
                c1 = False
            if y - 1 >= 0 and a[x][y] == a[x][y - 1]:
                c1 = False
    else:
        c1 = False

    c2 = True
    # 가로 검사
    if x + 4 <= 18:
        for i in range(1, 5):
            if a[x][y] != a[x + i][y]:
                c2 = False
                break
        else:
            if x + 5 <= 18 and a[x][y] == a[x + 5][y]:
                c2 = False
            if x - 1 >= 0 and a[x][y] == a[x - 1][y]:
                c2 = False
    else:
        c2 = False

    # 대각선 검사
    c3 = True
    if x + 4 <= 18 and y + 4 <= 18:
        for i in range(1, 5):
            if a[x][y] != a[x + i][y + i]:
                c3 = False
                break
        else:
            if y + 5 <= 18 and x + 5 <= 18 and a[x][y] == a[x + 5][y + 5]:
                c3 = False
            if x - 1 >= 0 and y - 1 >= 0 and a[x][y] == a[x - 1][y - 1]:
                c3 = False
    else:
        c3 = False

    c4 = True
    if x - 4 >= 0 and y + 4 <= 18:
        for i in range(1, 5):
            if a[x][y] != a[x - i][y + i]:
                c4 = False
                break
        else:
            if y + 5 <= 18 and x - 5 >= 0 and a[x][y] == a[x - 5][y + 5]:
                c4 = False
            if y - 1 >= 0 and x + 1 <= 18 and a[x][y] == a[x + 1][y - 1]:
                c4 = False
    else:
        c4 = False

    return c1 | c2 | c3 | c4

a = [list(map(int, input().split())) for _ in range(19)]
for i in range(19):
    for j in range(19):
        if a[i][j] != 0:
            if omok(i, j):
                print(a[i][j])
                print(i + 1, j + 1)
                sys.exit(0)

print(0)