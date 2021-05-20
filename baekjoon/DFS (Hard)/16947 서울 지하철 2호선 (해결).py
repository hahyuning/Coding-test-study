from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)

# 1. 순환선(시작점 = 도착점) 찾기 (DFS)
def find_cycle(x, prev):
    # 리턴값
    # -2: 사이클을 찾았으나 포함 X
    # -1: 사이클 못찾음
    # 0 ~ n - 1: 사이클에서 시작 인덱스

    # x를 이미 방문한 경우 사이클을 찾은 경우이므로 시작점 반환
    if check[x] == 1:
        return x
    # 방문 처리
    check[x] = 1

    for y in graph[x]:
        if y == prev:
            continue
        res = find_cycle(y, x)
        # 사이클을 찾은 경우 -2 리턴
        if res == -2:
            return -2
        # 사이클의 시작점 찾기
        if res >= 0:
            # 사이클 기록
            check[x] = 2
            # 시작점을 찾은 경우
            if x == res:
                return -2
            # 아닌 경우
            else:
                return res
    return -1

# 0. 입력
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# check
# 0: 방문 X, 1: 방문, 2: 사이클
check = [0] * (n + 1)
find_cycle(1, 0)

# 2. 정점과 순환선 사이의 거리 찾기 (BFS)
q = deque()
dist = [-1] * (n + 1)
for i in range(1, n + 1):
    if check[i] == 2:
        q.append(i)
        dist[i] = 0

while q:
    now = q.popleft()
    for nxt in graph[now]:
        if dist[nxt] == -1:
            q.append(nxt)
            dist[nxt] = dist[now] + 1

print(" ".join(map(str, dist[1:])))