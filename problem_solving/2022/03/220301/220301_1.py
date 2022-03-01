def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


t = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    parent = [i for i in range(n + 1)]
    cycle = set()

    for _ in range(m):
        a, b = map(int, input().split())
        x, y = find(a), find(b)

        if x == y:
            cycle.add(x)
        elif x in cycle or y in cycle:
            cycle.add(x)
            cycle.add(y)
        union(a, b)

    tree = set()
    for i in range(1, n + 1):
        x = find(i)
        if x not in cycle:
            tree.add(x)

    ans = len(tree)
    if ans == 0:
        print("Case {}: No trees.".format(t))
    elif ans == 1:
        print("Case {}: There is one tree.".format(t))
    else:
        print("Case {}: A forest of {} trees.".format(t, ans))
    t += 1

