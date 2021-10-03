x, y, p1, p2 = map(int, input().split())
check1 = [False] * 10001
check2 = [False] * 10001

for i in range(p1, 10001, x):
    check1[i] = True

for i in range(p2, 10001, y):
    check2[i] = True

ans = -1
for i in range(10001):
    if check1[i] and check2[i]:
        if ans == -1:
            ans = i
print(ans)