# 놀이기구 운행 시간이 mid 일때 탑승할 수 있는 아이의 수 리턴
def check(mid):
    ans = 0
    for x in a:
        ans += (mid - 1) // x + 1
    return ans

n, m = map(int, input().split())
a = list(map(int, input().split()))

if n <= m:
    print(n)
else:
    lt = 0
    rt = 30 * n
    # 탑승한 아이 수
    ans = 0
    # 놀이기구 운행 시간
    time = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        res1 = check(mid)
        res2 = check(mid + 1)
        if res1 < n <= res2:
            ans = res1
            time = mid
            break
        elif res2 < n:
            lt = mid + 1
        elif res1 >= n:
            rt = mid - 1

    for i in range(m):
        # 각 놀이기구 당 1분 후 태운 아이 수 더하기
        if time % a[i] == 0:
            ans += 1
        if ans >= n:
            print(i + 1)
            break
