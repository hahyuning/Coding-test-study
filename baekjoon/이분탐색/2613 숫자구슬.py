def check(mid):
    cnt = 1
    s = 0
    for i in range(n):
        s += a[i]
        if s > mid:
            s = a[i]
            cnt += 1
    return cnt

def make_group(ans):
    global m
    s = 0
    cnt = 0
    for i in range(n):
        s += a[i]
        if s > ans:
            s = a[i]
            m -= 1
            print(cnt, end=" ")
            cnt = 0
        cnt += 1
        if n - i == m:
            break

    for _ in range(m):
        print(cnt, end=" ")
        cnt = 1

n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
lt = max(a)
rt = sum(a)
while lt <= rt:
    mid = (lt + rt) // 2
    cnt = check(mid)
    if cnt > m:
        lt = mid + 1
    else:
        ans = mid
        rt = mid - 1

print(lt)
make_group(lt)