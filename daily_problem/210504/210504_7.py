from collections import Counter

n = int(input())
a = []
s = 0
for _ in range(n):
    x = int(input())
    s += x
    a.append(x)

print(round(s / n))

a.sort()
print(a[n // 2])

if len(a) == 1:
    print(a[0])
else:
    b = Counter(a)
    c = b.most_common(2)

    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])

print(a[n - 1] - a[0])

