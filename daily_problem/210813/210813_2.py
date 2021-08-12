s = input()
d = [[0] * 26 for _ in range(len(s) + 1)]

for i in range(1, len(s) + 1):
    x = ord(s[i - 1]) - ord("a")
    for j in range(26):
        if j == x:
            d[i][j] = d[i - 1][j] + 1
            continue
        d[i][j] = d[i - 1][j]

n = int(input())
for _ in range(n):
    x, l, r = input().split()
    x = ord(x) - ord("a")
    r = int(r)
    l = int(l)

    print(d[r + 1][x] - d[l][x])
