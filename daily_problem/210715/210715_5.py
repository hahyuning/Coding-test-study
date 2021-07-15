from bisect import bisect_left

m, n, l = map(int, input().split())
sadae = list(map(int, input().split()))
sadae.sort()
animal = []
for _ in range(n):
    a, b = map(int, input().split())
    animal.append((a, b))

cnt = 0
for x, y in animal:
    length = l - y
    idx = bisect_left(sadae, x)
    if idx == 0:
        if abs(sadae[0] - x) <= length:
            cnt += 1
    elif idx == m:
        if abs(sadae[-1] - x) <= length:
            cnt += 1
    else:
        if abs(sadae[idx - 1] - x) <= length or abs(sadae[idx] - x) <= length:
            cnt += 1
print(cnt)