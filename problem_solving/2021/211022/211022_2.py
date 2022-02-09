a = input()
duck = ["q", "u", "a", "c", "k"]
check = [False] * len(a)

if len(a) % 5 != 0:
    print(-1)
else:
    cnt = 0
    pnt = 0
    for i in range(len(a)):
        if a[i] == "q" and not check[i]:
            for j in range(len(a)):
                if duck[pnt] == a[j] and not check[j]:
                    check[j] = True
