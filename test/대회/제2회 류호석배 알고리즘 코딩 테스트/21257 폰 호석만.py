def base_change(n, x):
    ans = 0
    n = n[::-1]
    for i in range(len(n)):
        if n[i].isdigit():
            if int(n[i]) < x:
                ans += int(n[i]) * (x ** i)
            else:
                return -1
        else:
            if ord(n[i]) - ord("a") + 10 < x:
                ans += (ord(n[i]) - ord("a") + 10) * (x ** i)
            else:
                return -1
    return ans

a, b = input().split()
res = []
for i in range(2, 37):
    x = base_change(a, i)
    if x != -1 and x < 2 ** 63:
        for j in range(2, 37):
            if i == j:
                continue

            y = base_change(b, j)
            if x == y:
                res.append([x, i, j])

if len(res) == 1:
    print(*res[0])
elif len(res) > 1:
    print("Multiple")
else:
    print("Impossible")