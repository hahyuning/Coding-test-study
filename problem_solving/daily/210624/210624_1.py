from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for i in range(n):
        for j in range(i, n):
            if i == j:
                continue
            graph[a[i]][a[j]] = True
            indegree[a[j]] += 1

    for _ in range(m):
        b, c = map(int, input().split())
        if graph[b][c]:
            graph[b][c] = False
            indegree[c] -= 1
            graph[c][b] = True
            indegree[b] += 1
        else:
            graph[c][b] = False
            indegree[b] -= 1
            graph[b][c] = True
            indegree[c] += 1

    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    check = False
    res = []
    while q:
        now = q.popleft()
        res.append(now)
        cnt = 0
        for i in range(1, n + 1):
            if graph[now][i]:
                indegree[i] -= 1

                if indegree[i] == 0:
                    cnt += 1
                    q.append(i)
        if cnt >= 2:
            check = True
            break

    if check:
        print("?")
    elif len(res) == n:
        print(*res)
    else:
        print("IMPOSSIBLE")
