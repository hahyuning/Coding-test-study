while True:
    try:
        s = input()
        ans = [0] * 4
        for x in s:
            if x.isdigit():
                ans[2] += 1
            elif x.isalpha():
                if x.isupper():
                    ans[1] += 1
                else:
                    ans[0] += 1
            else:
                ans[3] += 1
        print(*ans)
    except:
        break