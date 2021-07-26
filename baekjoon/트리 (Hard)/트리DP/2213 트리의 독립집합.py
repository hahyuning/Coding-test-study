def dfs(start):
    visited[start] = True
    d[start][1] = w[start]
    trace[start][1].append(start)

    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(nxt)
            d[start][1] += d[nxt][0]
            trace[start][1] += trace[nxt][0]

            if d[nxt][0] > d[nxt][1]:
                d[start][0] += d[nxt][0]
                trace[start][0] += trace[nxt][0]
            else:
                d[start][0] += d[nxt][1]
                trace[start][0] += trace[nxt][1]

n = int(input())
w = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
trace = [[[], []] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# d[i][0]: 노드 i가 독립집합에 포함되지 않은 경우의 최댓값
# i의 각 자식들이 포함된 경우와 포함되지 않은 경우의 최댓값의 합
# d[i][1]: 노드 i가 독립집합에 포함된 경우의 최댓값
# i의 각 자식들이 포함되지 않은 경우의 합 + i의 가중치
d = [[0] * 2 for _ in range(n + 1)]
dfs(1)

if d[1][0] > d[1][1]:
    print(d[1][0])
    trace[1][0].sort()
    print(*trace[1][0])
else:
    print(d[1][1])
    trace[1][1].sort()
    print(*trace[1][1])