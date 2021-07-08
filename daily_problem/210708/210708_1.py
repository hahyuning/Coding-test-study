from collections import deque, defaultdict

t = int(input())
for _ in range(t):
    # k: 테스트케이스, m: 노드, p: 간선
    k, m, p = map(int, input().split())
    graph = [[] for _ in range(m + 1)]
    indegree = [0] * (m + 1)
    for _ in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    # 들어오는 간선 중 가장 큰 번호
    res = defaultdict(list)
    q = deque()
    for i in range(1, m + 1):
        if indegree[i] == 0:
            q.append((i, 1))
            res[i] = 1

    while q:
        now, s = q.popleft()
        if now == m:
            print(k, s)
            break
        for nxt in graph[now]:
            indegree[nxt] -= 1
            res[nxt].append(s)

            if indegree[nxt] == 0:
                tmp = res[nxt]
                max_val = max(tmp)
                if tmp.count(max_val) == 1:
                    q.append((nxt, max_val))
                else:
                    q.append((nxt, max_val + 1))
