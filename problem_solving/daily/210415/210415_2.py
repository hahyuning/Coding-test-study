t = int(input())
for _ in range(t):
    n = int(input())

    ans = []
    i = 0
    while n > 1:
        d = n % 2
        if d == 1:
            ans.append(i)
        n //= 2
        i += 1
    if n == 1:
        ans.append(i)

    print(" ".join(map(str, ans)))