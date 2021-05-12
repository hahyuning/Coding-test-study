def top_down(i, j):
    if i == j:
        return 0
    if d[i][j] != -1:
        return d[i][j]

    # 최소 비용
    ans = d[i][j]
    # 마지막에 합치는 비용
    last_cost = sum(file[i:j + 1])

    for k in range(i, j):
        tmp = top_down(i, k) + top_down(k + 1, j) + last_cost
        if ans == -1 or ans > tmp:
            ans = tmp

    d[i][j] = ans

    return d[i][j]

t = int(input())
for _ in range(t):
    n = int(input())
    file = list(map(int, input().split()))

    # d[i][j]: i부터 j번째 파일을 합치는 데 드는 비용
    # d[i][j] = min(d[i][k] + d[k + 1][j]), i <= k < j
    # 범위 처리가 어려우므로 top down 방식 사용
    d = [[-1] * n for _ in range(n)]
    print(top_down(0, n - 1))

# -----------------------------------------------------------------
t = int(input())
for _ in range(t):
    n = int(input())
    file = list(map(int, input().split()))

    # d[i][j]: i부터 j번째 파일을 합치는 데 드는 비용
    # d[i][j] = min(d[i][k] + d[k + 1][j]), i <= k < j
    d = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        d[i][i + 1] = file[i] + file[i + 1]

    # l은 길이, i는 시작점, j는 끝점
    for l in range(3, n + 1):
        for i in range(0, n - l + 1):
            j = i + l - 1
            ans = d[i][j]
            cost = sum(file[i:j + 1])
            for k in range(i, j):
                tmp = d[i][k] + d[k + 1][j] + cost

                if ans == 0 or ans > tmp:
                    ans = tmp
            d[i][j] = ans

    print(d[0][n - 1])
