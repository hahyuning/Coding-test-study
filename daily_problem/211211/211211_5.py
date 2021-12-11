from collections import defaultdict

n, x = map(int, input().split())
a = list(map(int, input().split()))

res = defaultdict(int)
s = sum(a[:x])
res[s] += 1
for i in range(0, n):
    if i + x >= n:
        break

    s -= a[i]
    s += a[i + x]
    res[s] += 1

ans = sorted(res.items(), key=lambda x:-x[0])
if ans[0][0] == 0:
    print("SAD")
else:
    print(ans[0][0])
    print(ans[0][1])