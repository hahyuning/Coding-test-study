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

v = 11
graph = [[], [2], [3], [1], [2, 5], [7], [5], [6], [5, 9], [10],
         [11], [8]]
d = [0] * 12
id = 0
stack = []
finished = [False] * 12
SCC = []

for i in range(1, v + 1):
    if d[i] == 0:
        dfs(i)

print(len(SCC))
for x in SCC:
    for y in x:
        print(y, end=" ")
    print()