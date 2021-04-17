n = int(input())
a = list(map(int, input().split()))

# d[i]: i번째 칸에 도착할 수 있는 최소 점프 횟수
d = [-1] * n
d[0] = 0

for i in range(1, n):
    for j in range(i):
        if d[j] != -1 and i - j <= a[j]:
            if d[i] == -1 or d[i] > d[j] + 1:
                d[i] = d[j] + 1

print(d[n - 1])