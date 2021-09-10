def solution(sales, links):
    n = len(sales)
    tree = [[] for _ in range(n + 1)]
    for a, b in links:
        tree[a].append(b)

    # d[i][0]: i 번째 사람이 워크숍에 참가하지 않았을 때의 최소값
    # d[i][1]: i 번째 사람이 워크숍에 참가했을 때의 최소값
    d = [[0] * 2 for _ in range(n + 1)]

    def dfs(now):
        d[now][1] = sales[now - 1]

        for nxt in tree[now]:
            dfs(nxt)
            d[now][1] += min(d[nxt][0], d[nxt][1])

        check = False
        tmp = 0
        tmp_list = []
        for nxt in tree[now]:
            # 워크숍에 참여시킬 팀원이 있는 경우
            if d[nxt][0] > d[nxt][1]:
                check = True
                tmp += d[nxt][1]
            else:
                tmp_list.append(d[nxt][1] - d[nxt][0])
                tmp += d[nxt][0]

        if tmp_list:
            if check:
                d[now][0] = tmp
            else:
                tmp_list.sort()
                d[now][0] = tmp + tmp_list[0]
        else:
            d[now][0] = tmp

    dfs(1)
    return min(d[1][0], d[1][1])
