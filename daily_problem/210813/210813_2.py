import sys
input = sys.stdin.readline

s = input().rstrip()
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
    x, l, r = input().rstrip().split()
    x = ord(x) - ord("a")
    r = int(r)
    l = int(l)

    ans = d[r + 1][x] - d[l][x]
    sys.stdout.write(str(ans) + "\n")
