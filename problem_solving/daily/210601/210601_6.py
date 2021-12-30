def check(s):
    lt = 0
    rt = len(s) - 1
    while lt < rt:
        if s[lt] == s[rt]:
            lt += 1
            rt -= 1
        else:
            return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    if s == s[::-1]:
        print(0)
    else:
        lt = 0
        rt = len(s) - 1
        flg = False
        ans = True
        while lt < rt:
            if s[lt] == s[rt]:
                lt += 1
                rt -= 1
            else:
                if not flg:
                    flg = True
                    res1 = check(s[lt + 1:rt + 1])
                    res2 = check(s[lt:rt])

                    if res1 == False and res2 == False:
                        ans = False
                    break
                else:
                    ans = False
                    break
        print(1 if ans else 2)

