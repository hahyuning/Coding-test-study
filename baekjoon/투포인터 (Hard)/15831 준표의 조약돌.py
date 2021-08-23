# 까만 조약돌을 b개 이하, 하얀 조약돌을 w개 이상
n, b, w = map(int, input().split())
a = input()

lt = 0
rt = 0
b_cnt = 0
w_cnt = 0

ans = 0
while rt < n:
    if a[rt] == "W":
        w_cnt += 1
    else:
        b_cnt += 1

    while b_cnt > b:
        if a[lt] == "W":
            w_cnt -= 1
        else:
            b_cnt -= 1
        lt += 1

    if w_cnt >= w:
        ans = max(ans, rt - lt + 1)
    rt += 1
print(ans)