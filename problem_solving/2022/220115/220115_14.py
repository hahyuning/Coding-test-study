n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.sort()
x_median = a[n // 2][0]
a.sort(key=lambda x: x[1])
y_median = a[(n - 1) // 2][1]

ans = 0
for x, y in a:
    ans += abs(x - x_median) + abs(y - y_median)
print(ans)