s = input().split(".")
ans = ""
for x in s:
    if x == "":
        ans += "."
    else:
        n = len(x)
        if n % 2 == 1:
            print(-1)
            break
        m = n // 4
        k = (n % 4) // 2
        ans += "AAAA" * m
        ans += "BB" * k
        ans += "."
else:
    print(ans[:-1])