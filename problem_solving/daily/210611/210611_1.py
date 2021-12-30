def match(n):
    global ans
    if n == 11:
        ans = max(ans, sum(check))
        return

    for i, x in enumerate(player):
        if check[i] == 0 and x[n] > 0:
            check[i] = x[n]
            match(n + 1)
            check[i] = 0
    return

t = int(input())
for _ in range(t):
    player = [list(map(int, input().split())) for _ in range(11)]
    check = [0] * 11
    ans = 0
    match(0)
    print(ans)