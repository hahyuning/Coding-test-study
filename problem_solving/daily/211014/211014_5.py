n = int(input())
h = list(map(int, input().split()))
a = list(map(int, input().split()))

x = [(i, j) for i, j in zip(a, h)]
x.sort()

ans = 0
for i in range(n):
    ans += x[i][1] + i * x[i][0]
print(ans)