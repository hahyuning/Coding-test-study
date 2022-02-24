t = int(input())
dic = {0:[0, 3, 6], 1:[1, 4, 7], 2:[2, 5, 8], 3:[0, 1, 2], 4:[3, 4, 5], 5:[6, 7, 8], 6:[0, 4, 8], 7:[2, 4, 6]}

for _ in range(t):
    a = []
    for _ in range(3):
        tmp = input().split()
        for x in tmp:
            if x == "H":
                a.append(0)
            else:
                a.append(1)

    ans = -1
    for i in range(1 << 8):
        b = a[:]
        cnt = 0
        for k in range(8):
            if (i & (1 << k)) > 0:
                cnt += 1
                tmp = dic[k]
                for x in tmp:
                    b[x] = 1 - b[x]

        if sum(b) == 0 or sum(b) == 9:
            if ans == -1 or cnt < ans:
                ans = cnt
    print(ans)
