def check(mid):
    need = 0
    for x in a:
        if x < mid:
            need += (mid - x)
    if need <= k:
        return True
    return False

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

lt = min(a)
rt = max(a) + k
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if check(mid):
        lt = mid + 1
        ans = mid
    else:
        rt = mid - 1
print(ans)