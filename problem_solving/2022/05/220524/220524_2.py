while True:
    s = input()
    if s == "*":
        break

    ans = False
    for d in range(1, len(s)):
        a = []
        for i in range(len(s) - d):
            tmp = s[i] + s[i + d]

            if tmp in a:
                ans = True
                break
            else:
                a.append(tmp)

        if ans:
            print(s + " is NOT surprising.")
            break
    else:
        print(s + " is surprising.")
