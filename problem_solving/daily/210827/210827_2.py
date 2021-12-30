import sys
input = sys.stdin.readline

def check(mid):
    res = 0
    for x in a:
        if x >= 2 * k:
            x -= 2 * k
            res += x // mid
        elif x >= k:
            x -= k
            res += x // mid
    return res

n, k, m = map(int, input().split())
a = []
for _ in range(n):
    x = int(input())
    a.append(x)

lt = 1
rt = max(a)

ans = -1
while lt <= rt:
    mid = (lt + rt) // 2
    res = check(mid)

    if res >= m:
        ans = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(ans)