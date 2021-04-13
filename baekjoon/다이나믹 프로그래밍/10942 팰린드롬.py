import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().rstrip().split()))

# d[i][j] = i부터 j까지의 팰린드롬 여부
d = [[False] * n for _ in range(n)]

for i in range(n):
    for start in range(n):
        end = start + i

        if end >= n:
            break

        if start == end:
            d[start][end] = True
            continue
        if start + 1 == end and num[start] == num[end]:
            d[start][end] = True
            continue

        if num[start] == num[end] and d[start + 1][end - 1]:
            d[start][end] = True

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(1 if d[s - 1][e - 1] else 0)
