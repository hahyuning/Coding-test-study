from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0

for i, x in enumerate(a):
    tmp = a[:i] + a[i + 1:]

    left = 0
    right = len(tmp) - 1

    while left < right:
        s = tmp[left] + tmp[right]
        if s < x:
            left += 1
        elif s > x:
            right -= 1
        else:
            ans += 1
            break

print(ans)