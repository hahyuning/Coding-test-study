n = int(input())
a = []
total = 0
for _ in range(n):
    x, y = map(int, input().split())
    a.append((x, y))
    total += y

a.sort(key=lambda x:x[0])

mid = (total + 1) // 2
cnt = 0
for x, y in a:
    cnt += y
    if cnt >= mid:
        print(x)
        break
