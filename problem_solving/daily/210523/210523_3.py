d = [0] * 41
e = [0] * 41

d[0] = 1
e[1] = 1

for i in range(2, 41):
    d[i] = d[i - 1] + d[i - 2]
    e[i] = e[i - 1] + e[i - 2]

t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n], end=" ")
    print(e[n])