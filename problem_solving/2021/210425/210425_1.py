import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

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
    b, c = map(int, input().split())
    print(top_down(b - 1, c - 1))