def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def solution(n, costs):
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    edges = []
    result = 0

    for x in costs:
        edges.append((x[2], x[0], x[1]))

    edges.sort()
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    return result