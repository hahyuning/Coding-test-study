n, w = map(int, input().split())
a = [int(input()) for _ in range(n)]

coin = 0
for i in range(n - 1):
    if a[i] < a[i + 1]:
        if w // a[i] > 0:
            coin += w // a[i]
            w -= coin * a[i]
    elif a[i] > a[i + 1]:
        w += coin * a[i]
        coin = 0

if coin > 0:
    w += coin * a[-1]
print(w)
