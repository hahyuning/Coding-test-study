def find(x):
    min_dist = -1
    min_node = -1

    for i in range(n):
        if s[i] == 1:
            if min_dist == -1 or dist[x][i] < min_dist:
                min_dist = dist[x][i]
                min_node = i
    return min_node

def solution(a, b):
    ans = dist[a][b]

    if s[a] == 1 and s[b] == 1:
        if t < ans:
            return t

    aa = find(a)
    bb = find(b)
    if aa != -1 and bb != -1:
        tmp = dist[a][aa] + t + dist[b][bb]

        if tmp < ans:
            ans = tmp
    return ans


n, t = map(int, input().split())
x = [0] * n
y = [0] * n
s = [0] * n
for i in range(n):
    a, b, c = map(int, input().split())
    s[i] = a
    x[i] = b
    y[i] = c

dist = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        dist[i][j] = abs(x[i] - x[j]) + abs(y[i] - y[j])
        dist[j][i] = abs(x[i] - x[j]) + abs(y[i] - y[j])

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(solution(a, b))
