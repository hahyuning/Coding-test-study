def rotation(key):
    m = len(key)
    res = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            res[j][m - 1 - i] = key[i][j]
    return res

def check(lock):
    n = len(lock) // 3
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 지도 확장
    ex_lock = [[0] * (3 * n) for _ in range(3 * n)]
    for i in range(n):
        for j in range(n):
            ex_lock[i + n][j + n] = lock[i][j]

    for _ in range(4):
        key = rotation(key)

        for i in range(n * 2):
            for j in range(n * 2):
                for x in range(m):
                    for y in range(m):
                        ex_lock[i + x][j + y] += key[x][y]

                if check(ex_lock):
                    return True

                for x in range(m):
                    for y in range(m):
                        ex_lock[i + x][j + y] -= key[x][y]

    return False