n = int(input())
a = [0] * 1001
max_y = 0
idx = 0
for _ in range(n):
    x, y = map(int, input().split())
    a[x] = y

    if y > max_y:
        max_y = y
        idx = x

ans = 0
left_max = 0
for i in range(idx + 1):
    if a[i] > left_max:
        left_max = a[i]
    ans += left_max

right_max = 0
for i in range(1000, idx, -1):
    if a[i] > right_max:
        right_max = a[i]
    ans += right_max

print(ans)