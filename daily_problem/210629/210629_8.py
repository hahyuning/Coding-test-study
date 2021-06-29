while True:
    try:
        s = input()
        ans = ""
        moum = ["a", "i", "y", "e", "o", "u"]
        jaum = ["b", "k", "x", "z", "n", "h", "d", "c", "w", "g", "p", "v", "j", "q", "t", "s", "r", "l", "m", "f"]
        for x in s:
            check = False
            if x.isalpha():
                if x.isupper():
                    check = True
                    x = chr(ord(x) + 32)
                if x in moum:
                    tmp = moum[(moum.index(x) + 3) % 6]
                else:
                    tmp = jaum[(jaum.index(x) + 10) % 20]

                if check:
                    ans += tmp.upper()
                else:
                    ans += tmp
            else:
                ans += x

        print(ans)
    except:
        break