import sys
sys.setrecursionlimit(10 ** 9)

def dfs(x):
    check[x] = True
    # x 마을을 포함하는 경우
    d[x][0] = people[x]
    # x 마을을 포함하지 않는 경우
    d[x][1] = 0

    for nx in graph[x]:
        if not check[nx]:
            dfs(nx)
            d[x][0] += d[nx][1]
            d[x][1] += max(d[nx][0], d[nx][1])

n = int(input())
people = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# d[i][j]: i번째 마을에서 우수 마을의 주민 수의 총 합, j가 0이면 i번째 마을 포함, j가 1이면 i번째 마을 미포함
d = [[0] * 2 for _ in range(n + 1)]
check = [False for _ in range(n + 1)]

dfs(1)
print(max(d[1][0], d[1][1]))