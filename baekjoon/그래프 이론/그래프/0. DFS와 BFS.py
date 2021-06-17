import collections
n, m, start = map(int, input().split())
dic = collections.defaultdict(list)

for _ in range(m):
    s, e = map(int, input().split())
    dic[s].append(e)
    dic[e].append(s)

for x, y in dic.items():
    y.sort()

# 방문 여부 확인
visited = [False] * (n + 1)

def dfs(x):
    global visited
    visited[x] = True
    print(x, end=" ")

    for i in dic[x]:
        # 이전에 방문하지 않은 경우
        if not visited[i]:
            dfs(i)

def bfs(x):
    check = [False] * (n + 1)
    q = collections.deque()
    check[x] = True
    q.append(x)

    while q:
        nx = q.popleft()
        print(nx, end= " ")
        for y in dic[nx]:
            if not check[y]:
                check[y] = True
                q.append(y)

dfs(start)
print()
bfs(start)