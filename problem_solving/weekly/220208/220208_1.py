import sys
input = sys.stdin.readline

def count(mid):
    cnt = 1
    now = house[0]
    for i in range(n - 1):
        if house[i + 1] - now >= mid:
            cnt += 1
            now = house[i + 1]
    return cnt


n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

lt = 1
rt = house[-1] - house[0]
ans = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= c:
        ans = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(ans)