INF = 1e9
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        dist[a][b] = c
        dist[b][a] = c
    for i in range(1, n + 1):
        dist[i][i] = 0

    k = int(input())
    friends = list(map(int, input().split()))

    for l in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][l] + dist[l][j])

    min_cost = -1
    room_num = -1
    for i in range(1, n + 1):
        tmp = 0
        for j in friends:
            tmp += dist[j][i]
        if min_cost == -1 or tmp < min_cost:
            min_cost = tmp
            room_num = i

    print(room_num)
