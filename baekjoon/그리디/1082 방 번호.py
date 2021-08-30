n = int(input())
cost = list(map(int, input().split()))
min_val = 50
min_num = 0
for i in range(1, n):
    if cost[i] <= min_val:
        min_num = i
        min_val = cost[i]

nxt_min_val = 50
nxt_min_num = 0
for i in range(n):
    if cost[i] <= nxt_min_val:
        nxt_min_num = i
        nxt_min_val = cost[i]

m = int(input())
if min_val > m:
    print(0)
else:
    ans = [min_num] + [nxt_min_num] * ((m - min_val) // nxt_min_val)
    m -= min_val
    m -= (m // nxt_min_val) * nxt_min_val

    for i in range(len(ans)):
        for j in range(n - 1, -1, -1):
            if i == 0:
                tmp = min_val - cost[j]
            else:
                tmp = nxt_min_val - cost[j]
            if m + tmp >= 0:
                m += tmp
                ans[i] = j
                break

    print("".join(map(str, ans)))
