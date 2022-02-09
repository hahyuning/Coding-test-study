# 일방 통행
# i에서 j로 갔다가 다시 돌아올 수 있으면 통제 가능
# 경찰서를 세우는 비용은 cost[i]

def dfs(x):
    global id
    id += 1
    d[x] = id
    stack.append(x)

    parent = d[x]
    for y in range(n):
        if graph[x][y] == 1:
            if d[y] == 0:
                parent = min(parent, dfs(y))
            elif not finished[y]:
                parent = min(parent, d[y])

    if parent == d[x]:
        scc = []
        while True:
            t = stack.pop()
            scc.append(t)
            finished[t] = True
            if t == x:
                break
        SCC.append(scc)

    return parent

n = int(input())
cost = list(map(int, input().split()))
graph = [list(map(int, list(input()))) for _ in range(n)]

d = [0] * n
id = 0
stack = []
finished = [False] * n
SCC = []

for i in range(n):
    if d[i] == 0:
        dfs(i)

ans = 0
for scc in SCC:
    min_cost = 1000000
    for x in scc:
        min_cost = min(min_cost, cost[x])
    ans += min_cost
print(ans)
