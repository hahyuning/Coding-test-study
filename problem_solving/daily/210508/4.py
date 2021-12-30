from collections import deque

def solution(n, start, end, roads, traps):
    answer = -1
    graph = [[[] for _ in range(n + 1)] for _ in range(2)]
    for a, b, c in roads:
        graph[0][a].append((b, c))
        graph[1][b].append((a, c))

    q = deque()
    q.append(start)
    dist = [[-1] * 2 for _ in range(n + 1)]
    dist[start][0] = 0

    now_dir = 0
    while q:

        print(q)
        print(dist)
        now = q.popleft()
        if now in traps:
            now_dir = 1 - now_dir

        for nxt, cost in graph[now_dir][now]:
            # 다음 칸이 함정인 경우
            if nxt in traps:
                now_dir = 1 - now_dir
                if dist[nxt][now_dir] == -1:
                    q.append(nxt)
                    dist[nxt][now_dir] = dist[now][now_dir] + cost

            # 다음 칸이 함정이 아닌 경우
            else:
                if dist[nxt][now_dir] == -1:
                    q.append(nxt)
                    dist[nxt][now_dir] = dist[now][now_dir] + cost

    return answer

solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2, 3])