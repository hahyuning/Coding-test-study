num = [[1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
       [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
       [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
       [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
       [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
       [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
       [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
       [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
       [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
       [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1]]

a = []
while True:
    try:
        x = input()
        a.append(x)
    except:
        break

if not a or len(a) != 5:
    print("BOOM!!")
else:
    n = len(a[0])
    b = []
    for j in range(0, n, 4):
        tmp = []
        for i in range(5):
            if j >= n or j + 1 >= n or j + 2 >= n:
                break
            tmp.append(1 if a[i][j] == "*" else 0)
            tmp.append(1 if a[i][j + 1] == "*" else 0)
            tmp.append(1 if a[i][j + 2] == "*" else 0)
        b.append(tmp)

    ans = True
    s = ""
    for x in b:
        if len(x) != 15:
            ans = False
            break
        else:
            if x not in num:
                ans = False
                break

            s += str(num.index(x))

    if not ans:
        print("BOOM!!")
    else:
        if int(s) % 6 != 0:
            print("BOOM!!")
        else:
            print("BEER!!")


