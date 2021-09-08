def solution(N, stages):
    res = dict()

    # 해당 스테이지에 도달한 플레이어의 수
    clear = len(stages)

    for i in range(1, N + 1):
        if clear == 0:
            res[i] = 0
            continue

        # 해당 스테이지에 도달했으나 클리어하지 못한 플레이어의 수
        cnt = stages.count(i)
        res[i] = cnt / clear
        clear -= cnt

    return sorted(res, key=lambda x: res[x], reverse=True)