from collections import deque

graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * 9

q = deque()
q.append(1)
visited[1] = True

while q:
    now = q.popleft()
    print(now, end=" ")

    for nxt in graph[now]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)
