t = int(input())
for _ in range(t):
    n = int(input())
    parent = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        parent[b] = a
    a, b = map(int, input().split())
    a_par = [a]
    b_par = [b]

    # 각 노드의 부모 노드가 루트일때까지 저장
    while parent[a]:
        a_par.append(parent[a])
        a = parent[a]
    while parent[b]:
        b_par.append(parent[b])
        b = parent[b]

    a_lev = len(a_par) - 1
    b_lev = len(b_par) - 1
    # 루트노드부터 부모노드가 같지 않을 때까지 비교
    while a_par[a_lev] == b_par[b_lev]:
        a_lev -= 1
        b_lev -= 1
    print(a_par[a_lev + 1])