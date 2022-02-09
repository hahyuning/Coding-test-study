import sys
input = sys.stdin.readline

m = int(input())
dist = [[1e9] * 52 for _ in range(52)]

for i in range(52):
    dist[i][i] = 0
for _ in range(m):
    s = input().rstrip().split(" => ")
    if s[0].isupper():
        a = ord(s[0]) - ord("A")
    else:
        a = ord(s[0]) - ord("a") + 26
    if s[1].isupper():
        b = ord(s[1]) - ord("A")
    else:
        b = ord(s[1]) - ord("a") + 26
    dist[a][b] = 1

for k in range(52):
    for a in range(52):
        for b in range(52):
            dist[a][b] = min(dist[a][k] + dist[k][b], dist[a][b])

ans = []
for a in range(52):
    for b in range(52):
        if dist[a][b] != 1e9 and dist[a][b] != 0:
            if a == b:
                continue

            if 0 <= a < 26:
                x = chr(a + 65)
            else:
                x = chr(a + 71)
            if 0 <= b < 26:
                y = chr(b + 65)
            else:
                y = chr(b + 71)
            ans.append(x + " => " + y)
print(len(ans))
for x in ans:
    print(x)

