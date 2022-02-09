from collections import defaultdict

t = int(input())
for _ in range(t):
    a = defaultdict(list)
    n = int(input())
    for _ in range(n):
        x, y = input().split()
        a[y].append(x)

    ans = 1
    for i, x in a.items():
        ans *= (len(x) + 1)
    print(ans - 1)