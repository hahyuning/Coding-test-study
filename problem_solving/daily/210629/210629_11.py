a = []
max_len = 0
for _ in range(5):
    s = input()
    max_len = max(max_len, len(s))
    a.append(s)

ans = ""
for j in range(max_len):
    for i in range(5):
        if j >= len(a[i]):
            continue
        ans += a[i][j]
print(ans)