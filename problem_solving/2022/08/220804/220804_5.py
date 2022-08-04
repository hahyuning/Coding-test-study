def solution(beginning, target):
    row = len(beginning)
    col = len(beginning[0])

    cnt1 = 0
    tmp1 = [x[:] for x in beginning]

    for x in range(row):
        if tmp1[x][0] != target[x][0]:
            cnt1 += 1
            for k in range(col):
                tmp1[x][k] = 1 - tmp1[x][k]

    for y in range(col):
        if tmp1[0][y] != target[0][y]:
            cnt1 += 1
            for k in range(row):
                tmp1[k][y] = 1 - tmp1[k][y]

    cnt2 = 0
    tmp2 = [x[:] for x in beginning]

    for y in range(col):
        if tmp2[0][y] != target[0][y]:
            cnt2 += 1
            for k in range(row):
                tmp2[k][y] = 1 - tmp2[k][y]

    for x in range(row):
        if tmp2[x][0] != target[x][0]:
            cnt2 += 1
            for k in range(col):
                tmp2[x][k] = 1 - tmp2[x][k]

    if check(tmp1, target) and check(tmp2, target):
        return min(cnt1, cnt2)
    else:
        if check(tmp1, target):
            return cnt1
        if check(tmp2, target):
            return cnt2
        return -1


def check(beginning, target):
    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            if beginning[i][j] != target[i][j]:
                return False
    return True

print(solution([[1]], [[1]]))