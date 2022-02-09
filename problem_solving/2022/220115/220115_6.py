s = input()
n = len(s)

if n % 5 != 0:
    print(-1)
else:
    check = [False] * len(s)
    target = "quack"
    ans = 0

    for i in range(n):
        if s[i] == "q" and not check[i]:
            pnt = 0
            same_duck = False

            for j in range(i, n):
                if s[j] == target[pnt] and not check[j]:
                    check[j] = True
                    if s[j] == "k":
                        if not same_duck:
                            ans += 1
                            same_duck = True
                        pnt = 0
                    else:
                        pnt += 1

    if sum(check) != n or ans == 0:
        print(-1)
    else:
        print(ans)
