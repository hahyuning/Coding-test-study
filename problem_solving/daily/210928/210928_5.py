d, k = map(int, input().split())

for nxt in range(1, k + 1):
    now = k - nxt
    day = d - 2

    while day > 0 and nxt >= now:
        nxt, now = now, nxt - now
        day -= 1

    if day == 0:
        print(nxt)
        print(now + nxt)
        break