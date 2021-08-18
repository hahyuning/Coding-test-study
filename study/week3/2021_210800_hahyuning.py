from collections import deque, defaultdict

n, l = map(int, input().split())
graph = defaultdict(dict)

for k in range(1, l + 1):
    num = list(map(int, input().split()))

    for i in range(len(num) - 2):
        if k not in graph[num[i]]:
            graph[num[i]][k] = [num[i + 1]]
        else:
            graph[num[i]][k].append(num[i + 1])

        if k not in graph[num[i + 1]]:
            graph[num[i + 1]][k] = [num[i]]
        else:
            graph[num[i + 1]][k].append(num[i])

print(graph)
s, e = map(int, input().split())
dist = [-1] * (n + 1)
q = deque()
q.append(s)
dist[s] = 0

while q:
    now = q.popleft()

    cnt = 0
    for tmp_list in graph[now].values():
        if now in tmp_list:
            for nxt in tmp_list:
                if dist[nxt] == -1:
                    q.appendleft(nxt)
                    dist[nxt] = dist[now]
        else:
            for nxt in tmp_list:
                if dist[nxt] == -1:
                    q.append(nxt)
                    dist[nxt] = dist[now] + 1

print(dist[e])
