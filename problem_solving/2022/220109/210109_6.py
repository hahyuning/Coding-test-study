n, h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

ans = ""
for i in range(n):
    check = False
    for j in range(w * i, w * (i + 1)):
        for k in range(h):
            if s[k][j] != "?":
                ans += s[k][j]
                check = True
                break
        if check:
            break
    if not check:
        ans += "?"

print(ans)