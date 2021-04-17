def top_down(i, j):
    if i == j:
        return 1
    if i + 1 == j:
        if a[i] == a[j]:
            return 1
        else:
            return 0

    # 메모이제이션
    if d[i][j] != -1:
        return d[i][j]

    if a[i] != a[j]:
        d[i][j] = 0
    else:
        d[i][j] = top_down(i + 1, j - 1)

    return d[i][j]


n = int(input())
a = list(map(int, input().split()))

# d[i][j]: i번째 부터 j번째 까지의 팰린드롬 여부
# 반복문 범위 정하기가 어렵기 때문에 탑다운 방식 사용
d = [[-1] * n for _ in range(n)]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(top_down(a - 1, b - 1))

# ---------------------------------------------------------------------
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [[0] * n for _ in range(n)]

for i in range(n):
    d[i][i] = 1
# 길이가 2인 팰린드롬 처리
for i in range(n - 1):
    if a[i] == a[i + 1]:
        d[i][i + 1] = 1

# k는 길이, i는 시작점, j는 끝점
for k in range(3, n + 1):
    for i in range(0, n - k + 1):
        j = i + k - 1
        if a[i] == a[j] and d[i + 1][j - 1] == 1:
            d[i][j] = True

m = int(sys.stdin.readline())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(d[s - 1][e - 1])
