n, target = map(int, input().split())
a = list(map(int, input().split()))
ans = -1

start = 0
end = n - 1

while start <= end:
    mid = (start + end) // 2

    if a[mid] == target:
        ans = mid
        break

    elif a[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

print(ans)