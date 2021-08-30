n, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x:x[1])

ans = 0
day = t - n
for w, p in a:
    ans += w + p * day
    day += 1

print(ans)