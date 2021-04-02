def solution(d, budget):
    if sum(d) <= budget:
        return len(d)

    d.sort()
    cnt = 0
    b_sum = 0
    while b_sum <= budget:
        b_sum += d[cnt]
        cnt += 1

    return cnt - 1