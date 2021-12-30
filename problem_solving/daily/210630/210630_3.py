n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
sushi += sushi[:k]

if n == k:
    print(d)
else:
    lt = 0
    x = set(sushi[lt:lt + k])
    if c in x:
        ans = len(x)
    else:
        ans = len(x) + 1
    while True:
        x = set(sushi[lt + 1:lt + k])
        if lt >= n:
            break
        x.add(sushi[lt + k])
        if c in x:
            tmp = len(x)
        else:
            tmp = len(x) + 1
        ans = max(tmp, ans)
        lt += 1
    print(ans)