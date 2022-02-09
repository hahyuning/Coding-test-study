def dfs(x):
    global id
    id += 1
    d[x] = id
    stack.append(x)

    parent = d[x]
    for y in graph[x]:
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
graph = [[] for _ in range(n + 1)]
for i in range(n):
    graph[i + 1].append(int(input()))

d = [0] * (n + 1)
id = 0
stack = []
finished = [False] * (n + 1)
SCC = []

for i in range(1, n + 1):
    if d[i] == 0:
        dfs(i)

max_val = 0
max_comp = []
for x in SCC:
    if len(x) == 1 and graph[x[0]][0] == x[0]:
        max_val += 1
        max_comp.append(x[0])
    elif len(x) > 1:
        max_val += len(x)
        max_comp += x

print(max_val)
max_comp.sort()
for x in max_comp:
    print(x)


