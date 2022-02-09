t = int(input())

for _ in range(t):
    j, n = map(int, input().split())
    box = []
    for _ in range(n):
        r, c = map(int, input().split())
        box.append(r * c)
    box.sort(reverse=True)

    ans = 0
    for x in box:
        if j <= 0:
            break

        j -= x
        ans += 1
    print(ans)