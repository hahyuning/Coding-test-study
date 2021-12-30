import sys

n, k = map(int, input().split())
lt = 0
rt = n // 2 + 1
while lt <= rt:
    mid = (lt + rt) // 2
    res = (mid + 1) * (n - mid + 1)
    if res == k:
        print("YES")
        sys.exit(0)

    if res > k:
        rt = mid - 1
    else:
        lt = mid + 1
print("NO")