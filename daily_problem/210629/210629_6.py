def check(x):
    for i in range(len(a)):
        if i == len(a) - 1 and n - a[i] > x:
            return False
        if i == 0 and a[i] > x:
            return False
        if i != len(a) - 1 and i != 0 and a[i + 1] - a[i] > 2 * x:
            return False
    return True

n = int(input())
m = int(input())
a = list(map(int, input().split()))

lt = 0
rt = n
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if not check(mid):
        lt = mid + 1
    else:
        rt = mid - 1
        ans = mid
print(ans)