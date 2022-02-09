n = int(input())
check = dict()

for _ in range(n):
    s = input()
    s_list = s.split(" ")

    for i, x in enumerate(s_list):
        if x[0].lower() not in check:
            check[x[0].lower()] = True
            s_list[i] = "[" + x[0] + "]" + x[1:]
            print(" ".join(s_list))
            break
    else:
        for i in range(len(s)):
            if s[i] == " ":
                continue
            if s[i].lower() not in check:
                print(s[:i] + "[" + s[i] + "]" + s[i + 1:])
                check[s[i].lower()] = True
                break
        else:
            print(s)
