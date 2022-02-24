n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x:(-x[0], x[1]))

ans = 0
max_val = 1
for x, y in a:
    tmp = 0
    for i, j in a:
        if x > i:
            continue
        if x < j:
            continue
        tmp += x - j

    if tmp >= max_val:
        max_val = tmp
        ans = x

print(ans)