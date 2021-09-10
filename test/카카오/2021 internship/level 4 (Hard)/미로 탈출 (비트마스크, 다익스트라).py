import heapq

def check(now, nxt, state, trap_idx):
    now_trap, nxt_trap = False, False
    if now in trap_idx:
        if (state & (1 << trap_idx[now])) > 0:
            now_trap = True
    if nxt in trap_idx:
        if (state & (1 << trap_idx[nxt])) > 0:
            nxt_trap = True

    return now_trap != nxt_trap

def find_nxt_state(nxt, state, trap_idx):
    if nxt in trap_idx:
        return state ^ (1 << trap_idx[nxt])
    return state

def solution(n, start, end, roads, trap):
    graph = [[] for _ in range(n + 1)]
    for a, b, c in roads:
        graph[a].append((b, c, False))
        graph[b].append((a, c, True))

    trap_idx = dict()
    for i, x in enumerate(trap):
        trap_idx[x] = i

    dist = [[-1] * (n + 1) for _ in range(2 ** len(trap))]
    q = []
    heapq.heappush(q, [0, start, 0])
    dist[0][start] = 0

    ans = -1
    while q:
        cost, now, state = heapq.heappop(q)
        if now == end:
            if ans == -1 or cost < ans:
                ans = cost
                continue

        if dist[state][now] != -1 and cost > dist[state][now]:
            continue

        for nxt, nxt_cost, reverse in graph[now]:
            res = check(now, nxt, state, trap_idx)

            if reverse != res:
                continue

            nxt_state = find_nxt_state(nxt, state, trap_idx)
            nxt_cost += cost

            if nxt_cost < dist[nxt_state][nxt] or dist[nxt_state][nxt] == -1:
                dist[nxt_state][nxt] = nxt_cost
                heapq.heappush(q, [nxt_cost, nxt, nxt_state])
    return ans

solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])