from bisect import bisect_left

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()

cnt = 0
ans = []

for x in a:
    idx = bisect_left(b, x)
    if idx >= m or b[idx] != x:
        cnt += 1
        ans.append(x)

print(cnt)
ans.sort()
print(" ".join(map(str, ans)))