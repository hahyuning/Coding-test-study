n, m = map(int, input().split())
a = list(map(int, input().split()))
max_val = max(a)
max_id = a.index(max_val)

ans = 0
left_max = a[0]
for i in range(max_id):
    left_max = max(left_max, a[i])
    ans += (left_max - a[i])

right_max = a[-1]
for i in range(m - 1, max_id, -1):
    right_max = max(right_max, a[i])
    ans += (right_max - a[i])

print(ans)