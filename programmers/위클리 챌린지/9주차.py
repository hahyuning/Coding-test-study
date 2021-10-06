from collections import deque

tree = [[] for _ in range(101)]


def bfs(start, check):
    res = 0
    q = deque()
    q.append(start)
    check[start] = True

    while q:
        now = q.popleft()
        res += 1
        for nxt in tree[now]:
            if not check[nxt]:
                check[nxt] = True
                q.append(nxt)
    return res


def solution(n, wires):
    for x, y in wires:
        tree[x].append(y)
        tree[y].append(x)

    ans = n
    for i in range(1, n + 1):
        if len(tree[i]) > 0:
            for j in range(len(tree[i])):
                check = [False] * (n + 1)
                check[tree[i][j]] = True
                res1 = bfs(i, check)
                res2 = n - res1

                ans = min(ans, abs(res1 - res2))
    return ans