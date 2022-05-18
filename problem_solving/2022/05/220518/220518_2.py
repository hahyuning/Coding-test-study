def check(mid):
    cnt = 0
    s = 0
    for x in a:
        if x + s > mid:
            cnt += 1
            s = x
        elif x + s == mid:
            cnt += 1
            s = 0
        else:
            s += x

    if s != 0:
        cnt += 1
    return cnt

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    rt = sum(a)
    lt = max(a)
    ans = 0
    while lt <= rt:
        mid = (lt + rt) // 2

        if check(mid) > m:
            lt = mid + 1
        else:
            ans = mid
            rt = mid - 1

    print(ans)


