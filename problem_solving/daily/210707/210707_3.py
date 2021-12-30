import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

# 오일러 경로: 연결 그래프이면서 차수가 홀수인 간선이 0개 또는 2개
def dfs(now, num, cnt):
    global ans
    # 모든 간선을 다 탐색한 경우
    if cnt == e:
        ans = True
        return

    for nxt in graph[now]:
        # 이미 탐색한 간선인지 확인
        if check[now][nxt] == num or check[nxt][now] == num:
            continue

        check[now][nxt] = num
        check[nxt][now] = num
        dfs(nxt, num, cnt + 1)
    return

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = [[0] * (e + 1) for _ in range(e + 1)]
ans = False
for i in range(1, v + 1):
    dfs(i, i, 0)
    if ans:
        break

if ans:
    print("YES")
else:
    print("NO")