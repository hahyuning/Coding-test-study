import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
result = list(input().rstrip())
start = sorted(result)

up, down = [], []
for _ in range(n):
    tmp = list(input().rstrip())

    if tmp[0] == "?":
        up = down
        down = []
        continue
    down.append(tmp)

for i in range(len(up)):
    for j in range(k - 1):
        if up[i][j] == "-":
            start[j], start[j + 1] = start[j + 1], start[j]

for i in range(len(down) - 1, -1, -1):
    for j in range(k - 1):
        if down[i][j] == "-":
            result[j], result[j + 1] = result[j + 1], result[j]

ans = ["*" for _ in range(k - 1)]
for i in range(k - 1):
    if start[i] == result[i + 1] and start[i + 1] == result[i]:
        ans[i] = "-"
        start[i], start[i + 1] = start[i + 1], start[i]

if start == result:
    print("".join(ans))
else:
    print("x" * (k - 1))