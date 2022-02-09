n = int(input())
a = list(input())
m = len(a)
for _ in range(n - 1):
    b = list(input())
    for j in range(m):
        if a[j] != b[j]:
            a[j] = '?'

print(''.join(a))