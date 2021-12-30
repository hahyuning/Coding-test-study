n = int(input())
a = []
max_d = 0
for _ in range(n):
    p, d = map(int, input().split())
    max_d = max(max_d, d)
    a.append((d, p))
a.sort(key=lambda x:(-x[1], x[0]))

check = [False] * (max_d + 1)
ans = 0
for d, p in a:

    for i in range(d, 0, -1):
        if not check[i]:
            check[i] = True
            ans += p
            break

print(ans)