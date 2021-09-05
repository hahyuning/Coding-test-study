n = int(input())
s = input()
a = []
for _ in range(n):
    a.append(input())

ans = 0
for x in a:
    xm = len(x)
    sm = len(s)
    check = False
    for k in range(1, xm):
        for i in range(xm):
            tmp = ""
            for j in range(i, xm, k):
                tmp += x[j]

                if len(tmp) == sm:
                    if tmp == s:
                        check = True
                    break
    if check:
        ans += 1
print(ans)
