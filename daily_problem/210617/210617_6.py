n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
check = [[True] * n for _ in range(n)]

ans = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or j == k or k == i:
                continue

            # 다른 곳을 거치는 최단거리가 존재하는 경우 다리 제거
            if dist[i][j] == dist[i][k] + dist[k][j]:
                check[i][j] = False
            # 잘못된 플로이드 워셜
            elif dist[i][j] > dist[i][k] + dist[k][j]:
                ans = -1

if ans == -1:
    print(ans)
else:
    for i in range(n):
        for j in range(i, n):
            if check[i][j]:
                ans += dist[i][j]
    print(ans)
