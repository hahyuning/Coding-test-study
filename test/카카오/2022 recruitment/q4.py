def solution(n, info):
    result = []

    def check(idx, cnt, res1, res2):
        if sum(cnt) > n:
            return

        if idx == 11:
            if sum(cnt) == n:
                if res1 > res2:
                    result.append([res1 - res2, cnt])
            return

        for i in range(n + 1):
            tmp = cnt[:]
            tmp[idx] = i

            if i == 0 and info[idx] == 0:
                check(idx + 1, tmp, res1, res2)
                continue

            if i > info[idx]:
                check(idx + 1, tmp, res1 + 10 - idx, res2)
            else:
                check(idx + 1, tmp, res1, res2 + 10 - idx)

    check(0, [0] * 11, 0, 0)

    if not result:
        return [-1]

    result.sort(key=lambda x:(-x[0], x[1]))
    return result[0][1]

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
