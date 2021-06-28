x, y = map(int, input().split())
lt = 0
rt = 1000000000

ans = -1
while lt <= rt:
    mid = (lt + rt) // 2
    if (y + mid) * 100 // (x + mid) > y * 100 // x:
        ans = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(ans)