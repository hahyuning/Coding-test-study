def solution(n, lost, reserve):

    n_reserve = [r for r in reserve if r not in lost]
    n_lost = [l for l in lost if l not in reserve]

    for x in n_reserve:
        if x - 1 in n_lost:
            n_lost.remove(x - 1)
        elif x + 1 in n_lost:
            n_lost.remove(x + 1)
    answer = n - len(n_lost)
    return answer