n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = []
for i in range(n - k + 1):
    tmp = 0
    for j in range(i, i + k):
        tmp += a[j]
    ans.append(tmp)
print(max(ans))