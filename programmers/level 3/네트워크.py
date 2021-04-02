def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    parent = [0] * n
    for i in range(n):
        parent[i] = i

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                union_parent(parent, i, j)

    answer = set()
    for i in range(n):
        answer.add(find_parent(parent, i))

    return len(answer)