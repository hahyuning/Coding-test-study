def row_bingo(x):
    global cnt
    if row_check[x]:
        return

    for j in range(5):
        if not check[x][j]:
            return

    cnt += 1
    row_check[x] = True
    return

def col_bingo(y):
    global cnt
    if col_check[y]:
        return

    for i in range(5):
        if not check[i][y]:
            return

    cnt += 1
    col_check[y] = True
    return

def dig_bingo():
    global cnt
    if dig_check[0] and dig_check[1]:
        return

    flag = False
    if not dig_check[1]:
        for k in range(5):
            if not check[k][4 - k]:
                flag = True
        if not flag:
            cnt += 1
            dig_check[1] = True

    flag = False
    if dig_check[0]:
        for k in range(5):
            if not check[k][k]:
                flag = True
        if not flag:
            cnt += 1
            dig_check[0] = True
    return


a = [list(map(int, input().split())) for _ in range(5)]
check = [[False] * 5 for _ in range(5)]
row_check = [False] * 5
col_check = [False] * 5
dig_check = [False] * 2
order = [0]
for _ in range(5):
    order += list(map(int, input().split()))

cnt = 0
for k in range(1, 26):
    num = order[k]
    x, y = 0, 0
    for i in range(5):
        for j in range(5):
            if a[i][j] == num:
                check[i][j] = True

                row_bingo(i)
                col_bingo(j)
                if i == j or i + j == 4:
                    dig_bingo()

    if cnt >= 3:
        print(k)
        break


