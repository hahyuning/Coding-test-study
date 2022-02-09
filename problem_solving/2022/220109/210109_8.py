import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
zigzag = [0] * n

for i in range(2, n):
    if a[i] >= a[i - 1] >= a[i - 2] or a[i] <= a[i - 1] <= a[i - 2]:
        zigzag[i] = 0
    else:
        zigzag[i] = 1

ans = 0
for i in range(n):
    tmp = 0
    for j in range(i, n):
        if zigzag[j] == 0:
            break
        tmp += 1
    ans = max(ans, tmp)
print(ans + 2)