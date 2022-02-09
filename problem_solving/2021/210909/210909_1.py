while True:
    try:
        ans = 0
        n, m = map(int, input().split())
        for x in range(n, m + 1):
            x = str(x)
            if len(set(x)) == len(x):
                ans += 1
        print(ans)
    except:
        break