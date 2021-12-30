import sys
sys.setrecursionlimit(10 ** 5)

def dfs(now, day):
    if day == n:
        for i in range(1, n + 1):
            print(route[i])
        sys.exit(0)

    for nxt in rice_cake[day + 1]:
        if nxt != now and not check[nxt][day + 1]:
            check[nxt][day + 1] = True
            route[day + 1] = nxt
            dfs(nxt, day + 1)
    return

n = int(input())
rice_cake = dict()
check = [[False] * (n + 1) for _ in range(10)]

for i in range(1, n + 1):
    m, *a = map(int, input().split())
    rice_cake[i] = a

for x in rice_cake[1]:
    if not check[x][1]:
        check[x][1] = True
        route = [0] * (n + 1)
        route[1] = x
        dfs(x, 1)

print(-1)
