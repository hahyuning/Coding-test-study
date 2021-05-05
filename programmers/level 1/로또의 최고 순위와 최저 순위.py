def solution(lottos, win_nums):
    zero_cnt = 0
    for x in lottos:
        if x == 0:
            zero_cnt += 1

    lottos = set(lottos)
    win_nums = set(win_nums)

    ok = len(win_nums.intersection(lottos))
    if ok <= 1:
        if ok + zero_cnt <= 1:
            return [6, 6]
        else:
            return [7 - (ok + zero_cnt), 6]

    return [7 - (ok + zero_cnt), 7 - ok]

