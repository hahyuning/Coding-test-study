n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

ans = 0
for x in a:
    if x <= b:
        ans += 1
        continue

    ans += 1
    x -= b

    m, d = divmod(x, c)
    ans += m
    if d > 0:
        ans += 1

print(ans)