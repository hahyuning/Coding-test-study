cnt = 1
while True:
    # l: 사용 기간, p: 이용 가능 기간, v: 휴가 기간
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break

    ans = 0
    n, d = divmod(v, p)
    ans += n * l
    ans += min(l, d)

    print("Case " + str(cnt) + ": " + str(ans))
    cnt += 1
