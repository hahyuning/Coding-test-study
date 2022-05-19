n, l, w, h = map(int, input().split())
rt = min(l, w, h)
lt = 0

for _ in range(1000):
    mid = (lt + rt) / 2

    if (l // mid) * (w // mid) * (h // mid) >= n:
        lt = mid
    else:
        rt = mid

print("%.10f" % rt)
