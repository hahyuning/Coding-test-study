a, b = input().split()
n = len(a)
m = len(b)

ans = n
for start in range(m - n + 1):
    cnt = 0
    for i in range(n):
        if a[i] != b[start + i]:
            cnt += 1
    ans = min(ans, cnt)
print(ans)