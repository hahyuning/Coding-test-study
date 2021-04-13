num_list = [int(input()) for _ in range(7)]

min_odd = 101
min_sum = 0

for x in num_list:
    if x % 2 != 0:
        min_sum += x
        min_odd = min(min_odd, x)

if min_sum == 0:
    print(-1)
else:
    print(min_sum)
    print(min_odd)