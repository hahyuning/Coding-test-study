def solution(i, route):
    if d[i][route] != -1:
        return d[i][route]

    # 모든 도시를 다 방문한 경우
    if route == (1 << (n - 1)) - 1:
        if w[i][0]:
            return w[i][0]
        else:
            return 1e9

    min_val = 1e9
    for j in range(1, n):
        # i번째 도시에서 j번째 도시를 갈 수 없는 경우
        if not w[i][j]:
            continue

        # j번째 도시를 이미 방문한 경우
        if route & (1 << (j - 1)):
            continue

        dist = w[i][j] + solution(j, route | (1 << (j - 1)))
        min_val = min(min_val, dist)

    d[i][route] = min_val
    return d[i][route]


n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

# d[i][j]: i에서 시작해서 j에 포함된 루트를 방문한 후 0으로 돌아오는 최소비용
d = [[-1] * (1 << (n - 1)) for _ in range(n)]
print(solution(0, 0))