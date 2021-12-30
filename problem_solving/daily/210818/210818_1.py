n = int(input())
a = []
for _ in range(n):
    t, s = map(int, input().split())
    a.append((t, s))
a.sort(key=lambda x:x[1], reverse=True)

start = a[0][1]
end = start - a[0][0]
for i in range(1, n):
    if a[i][1] < end:
        start = a[i][1]
    else:
        start = end
    end = start - a[i][0]

if end < 0:
    print(-1)
else:
    print(end)