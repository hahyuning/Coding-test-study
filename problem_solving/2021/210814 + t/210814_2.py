n = int(input())
a = []
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    a.append((sm * 100 + sd, em * 100 + ed))
a.sort()

idx = -1
tmp = 0
ans = 0
now = 301

while now <= 1130 and idx < n:
    check = False
    idx += 1
    for i in range(idx, n):
        # 꽃이 피는 시간이 현재 시간보다 큰 경우
        if a[i][0] > now:
            break

        # 꽃이 지는 시간이 현재 시간보다 큰 경우
        # 현재시간 갱신
        if a[i][1] > tmp:
            tmp = a[i][1]
            idx = i
            check = True

    if check:
        now = tmp
        ans += 1
    else:
        print(0)
        break
else:
    print(ans)


