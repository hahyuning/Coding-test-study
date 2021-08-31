from collections import defaultdict

n, m, k = map(int, input().split())

# graph[i] : i를 건설한 후 건설할 수 있는 건물 번호 저장
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 현재 건설 되있는 건물 번호
construct = defaultdict(int)
check = True
for _ in range(k):
    a, x = map(int, input().split())
    # 건설
    if a == 1:
        # 건설할 수 없는 건물을 건설한 경우
        if indegree[x] != 0:
            check = False
            break

        construct[x] += 1
        if construct[x] == 1:
            for y in graph[x]:
                indegree[y] -= 1
    # 파괴
    else:
        # 건설한 적 없는 건물을 파괴한 경우
        if x not in construct or construct[x] <= 0:
            check = False
            break

        construct[x] -= 1
        if construct[x] == 0:
            for y in graph[x]:
                indegree[y] += 1

    if not check:
        break

print("King-God-Emperor" if check else "Lier!")