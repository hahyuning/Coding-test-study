def solution(beginning, target):
    ans = -1

    n = len(beginning) + len(beginning[0])
    m = len(beginning)
    l = len(beginning[0])

    if check(beginning, target):
        return 0

    for i in range(1, 1 << n):
        tmp = [x[:] for x in beginning]
        cnt = 0

        for j in range(n):
            if i & (1 << j):
                cnt += 1
                # 열 바꾸기
                if j >= m:
                    j -= m
                    for k in range(m):
                        tmp[k][j] = 1 - tmp[k][j]

                # 행 바꾸기
                else:
                    for k in range(l):
                        tmp[j][k] = 1 - tmp[j][k]

        if check(tmp, target):
            if ans == -1 or cnt < ans:
                ans = cnt
    return ans


def check(tmp, target):
    for i in range(len(tmp)):
        for j in range(len(tmp[0])):
            if tmp[i][j] != target[i][j]:
                return False
    return True

print(solution([[1]], [[1]]))