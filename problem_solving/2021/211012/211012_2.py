import sys
input = sys.stdin.readline

while True:
    try:
        s = input().rstrip().split()
        check = [False] * 6
        idx = []

        # 5번 확인
        if "dip" not in s:
            check[5] = True
        # 4번 확인
        if "jiggle" == s[0]:
            check[4] = True
        # 3번 확인
        if "twirl" in s:
            if "hop" not in s:
                check[3] = True
        # 2번 확인
        if len(s) < 3 or " ".join(s[-3:]) != "clap stomp clap":
            check[2] = True
        # 1번 확인
        for i in range(len(s)):
            if s[i] == "dip":
                if i == 0:
                    if s[i + 1] != "twirl":
                        idx.append(i)
                        check[1] = True
                elif i == len(s) - 1:
                    if i == 1:
                        if s[i - 1] != "jiggle":
                            idx.append(i)
                            check[1] = True
                    else:
                        if s[i - 1] != "jiggle" and s[i - 2] != "jiggle":
                            idx.append(i)
                            check[1] = True
                else:
                    if i == 1:
                        if s[i - 1] != "jiggle" and s[i + 1] != "twirl":
                            idx.append(i)
                            check[1] = True
                    else:
                        if s[i - 1] != "jiggle" and s[i - 2] != "jiggle" and s[i + 1] != "twirl":
                            idx.append(i)
                            check[1] = True

        if sum(check) == 0:
            print("form ok: " + " ".join(s))
        elif sum(check) == 1:
            ans = "form error "
            for i in range(1, 6):
                if check[i]:
                    if i == 1:
                        ans += "1:"
                        for j in range(len(s)):
                            if j in idx:
                                ans += " DIP"
                            else:
                                ans += " " + s[j]
                    else:
                        ans += str(i) + ": "
                        ans += " ".join(s)
            print(ans)
        else:
            ans = "form errors "
            tmp = []
            for i in range(1, 6):
                if check[i]:
                    tmp.append(str(i))
            ans += ", ".join(tmp[:-1])
            ans += " and " + tmp[-1]

            if "1" in tmp:
                ans += ":"
                for j in range(len(s)):
                    if j in idx:
                        ans += " DIP"
                    else:
                        ans += " " + s[j]
            else:
                ans += ": "
                ans += " ".join(s)
            print(ans)
    except:
        break
