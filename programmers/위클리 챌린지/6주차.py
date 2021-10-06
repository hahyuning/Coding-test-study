from collections import defaultdict


def solution(weights, head2head):
    ans = []
    cnt = defaultdict(int)
    rate = defaultdict(int)

    n = len(head2head)
    for i in range(n):
        tmp = 0
        all = 0
        for j in range(n):
            if head2head[i][j] == "W":
                all += 1
                tmp += 1
                if weights[i] < weights[j]:
                    cnt[i] += 1
            elif head2head[i][j] == "L":
                all += 1

        if all != 0:
            rate[i] = tmp / all

    for i in range(n):
        ans.append((rate[i], cnt[i], weights[i], i))
    ans.sort(key=lambda x: (x[0], x[1], x[2], -x[3]), reverse=True)

    return [x[3] + 1 for x in ans]