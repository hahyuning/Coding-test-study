import sys
n, m = map(int,input().split())
# 간선 리스트
edges = []
# 인접 행렬
a = [[False] * n for _ in range(n)]
# 인접 리스트
g = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int,input().split())
    # 간선 리스트 저장
    edges.append((u,v))
    edges.append((v,u))
    # 인접 행렬 저장
    a[u][v] = a[v][u] = True
    # 인접 리스트 저장
    g[u].append(v)
    g[v].append(u)

m *= 2
for i in range(m):
    for j in range(m):
        A, B = edges[i]
        C, D = edges[j]
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        # b와 c가 친구 관계가 아닌 경우
        if not a[B][C]:
            continue
        # 인접 행렬 확인
        for E in g[D]:
            if A == E or B == E or C == E or D == E:
                continue
            print(1)
            sys.exit(0)
print(0)
