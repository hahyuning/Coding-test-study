from itertools import combinations

def solution(orders, course):
    for i in range(len(orders)):
        orders[i] = sorted(list(orders[i]))

    ans = []
    for x in course:
        comb = set(combinations(orders[0], x))
        for i in range(1, len(orders)):
            comb = comb | set(combinations(orders[i], x))

        max_val = 0
        tmp = []
        for y in comb:
            y_set = set(y)
            cnt = 0
            for z in orders:
                if y_set.intersection(z) == y_set:
                    cnt += 1

            if cnt < 2:
                continue

            if cnt >= max_val:
                if cnt == max_val:
                    tmp.append("".join(y))
                else:
                    tmp = ["".join(y)]
                max_val = cnt
        ans += tmp
    return sorted(ans)

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])