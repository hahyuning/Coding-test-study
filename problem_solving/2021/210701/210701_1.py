n = int(input())
material = []
for _ in range(n):
    a, b = map(int, input().split())
    material.append((a, b))

ans = -1
for i in range(1, 1 << n):
    s = 1
    t = 0
    for k in range(n):
        if (i & (1 << k)) > 0:
            s *= material[k][0]
            t += material[k][1]
    if ans == -1 or abs(s - t) < ans:
        ans = abs(s - t)
print(ans)