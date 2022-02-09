t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    while a:
        x = a.pop()

        for i in range(len(a) - 1, -1, -1):
            if x >= a[i]:
                ans += (x - a[i])
                a.pop()
            else:
                break
    print(ans)
