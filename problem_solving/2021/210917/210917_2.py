def check(mid):
    cnt = 0
    prev = 0
    for x in s:
        if x - prev >= mid:
            cnt += 1
            prev = x
    return cnt

n, m, l = map(int, input().split())
s = [int(input()) for _ in range(m)]
s.append(l)

for _ in range(n):
    q = int(input())

    lt = 0
    rt = l
    ans = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        cnt = check(mid)
        if cnt > q:
            ans = max(ans, mid)
            lt = mid + 1
        else:
            rt = mid - 1
    print(ans)