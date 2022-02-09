t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    ans = 0
    for i in range(n, m + 1):
        num = str(i)
        ans += num.count("0")
    print(ans)