from collections import deque

t = int(input())
for _ in range(t):
    # 편의점 개수
    n = int(input())
    hx, hy = map(int, input().split())
    shop = [[hx, hy]] + [list(map(int, input().split())) for _ in range(n)]
    fx, fy = map(int, input().split())
    shop.append([fx, fy])

    if abs(hx - fx) + abs(hy - fy) <= 20:
        print("happy")
    else:
        dist = [-1] * (n + 2)
        graph = [[] for _ in range(n + 2)]
        for i in range(n + 2):
            for j in range(i, n + 2):
                if i == j:
                    continue

                d = abs(shop[i][0] - shop[j][0]) + abs(shop[i][1] - shop[j][1])
                if d / 50 <= 20:
                    graph[i].append(j)
                    graph[j].append(i)

        dist[0] = 0
        q = deque()
        q.append(0)

        while q:
            now = q.popleft()
            for nxt in graph[now]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[now] + 1
                    q.append(nxt)

        print("happy" if dist[-1] != -1 else "sad")
