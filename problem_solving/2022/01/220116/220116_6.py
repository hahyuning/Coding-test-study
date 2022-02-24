n, m = map(int, input().split())
a = [input() for _ in range(n)]
k = int(input())

ans = 0
for row in a:
    zero_cnt = 0
    for x in row:
        if x == "0":
            zero_cnt += 1

    cnt = 0
    if zero_cnt <= k and zero_cnt % 2 == k % 2:
        for row2 in a:
            if row == row2:
                cnt += 1
    ans = max(ans, cnt)

print(ans)