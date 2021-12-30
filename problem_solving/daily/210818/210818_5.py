s = input()
if "_" in s:
    if s[0] == "_" or s[-1] == "_" or "__" in s:
        print("Error!")

    else:
        ans = ""
        check = False

        for x in s:
            if x.isupper():
                print("Error!")
                break

            if x == "_":
                check = True
                continue

            if check:
                ans += x.upper()
                check = False
                continue
            ans += x
        else:
            print(ans)
else:
    if s[0].isupper():
        print("Error!")
    else:
        ans = ""
        for x in s:
            if x.isupper():
                ans += "_" + x.lower()
            else:
                ans += x
        print(ans)