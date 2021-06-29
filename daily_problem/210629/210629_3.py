# 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
# 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

while True:
    s = input()
    if s == "end":
        break

    moum = ["a", "e", "i", "o", "u"]
    check1 = False
    for x in moum:
        if x in s:
            check1 = True
            break

    if not check1:
        print("<" + s + "> is not acceptable.")
    else:
        check2 = True
        for i in range(len(s) - 2):
            cnt = 0
            for j in range(3):
                if s[i + j] in moum:
                    cnt += 1
                else:
                    cnt -= 1

            if cnt <= -3 or cnt >= 3:
                check2 = False
                break

        if not check2:
            print("<" + s + "> is not acceptable.")
        else:
            check3 = True
            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    if s[i] != "e" and s[i] != "o":
                        check3 = False
                        break

            if not check3:
                print("<" + s + "> is not acceptable.")
            else:
                print("<" + s + "> is acceptable.")



