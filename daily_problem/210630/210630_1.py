n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = []
i = 0
j = 0
while i < n and j < m:
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

if i < n:
    c += a[i:]
elif j < m:
    c += b[j:]

print(*c)