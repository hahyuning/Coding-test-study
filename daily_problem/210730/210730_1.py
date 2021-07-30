from bisect import bisect_left

l = int(input())
s = list(map(int, input().split()))
s.sort()
n = int(input())
idx = bisect_left(s, n)

if s[idx] == n:
    print(0)
else:
    if idx == 0:
        rt = s[0]
        lt = 0
    else:
        rt = s[idx]
        lt = s[idx - 1]

    ans = 0
    for i in range(lt + 1, rt):
        for j in range(i, rt):
            if i == j:
                continue
            if i <= n <= j:
                ans += 1
    print(ans)


