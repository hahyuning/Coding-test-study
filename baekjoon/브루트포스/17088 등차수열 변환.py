n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(0)
else:
    ans = -1
    for c1 in range(-1, 2):
        for c2 in range(-1, 2):
            cnt = 0
            if c1 != 0:
                cnt += 1
            if c2 != 0:
                cnt += 1

            a0 = a[0] + c1
            diff = (a[1] + c2) - a0

            check = False
            an = a0 + diff

            for i in range(2, n):
                an += diff

                if a[i] == an:
                    continue
                if a[i] - 1 == an or a[i] + 1 == an:
                    cnt += 1
                else:
                    check = True

            if not check:
                if ans == -1 or cnt < ans:
                    ans = cnt
    print(ans)