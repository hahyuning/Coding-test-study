n, m = map(int, input().split())
num_list = list(map(int, input().split()))

interval_sum = 0
result = []
pt = 0

for i in range(n):

    while pt < n and interval_sum < m:
        interval_sum += num_list[pt]
        pt += 1

    if interval_sum >= m:
        result.append(pt - i)

    interval_sum -= num_list[i]

if result:
    print(min(result))
else:
    print(0)
