n, k = map(int, input().split())

i = 0
ans = 0
for j in range(1, n + 1):
    if n % j == 0:
        i += 1
    if i == k:
        ans = j
        break

if i < k:
    print(0)
else:
    print(ans)