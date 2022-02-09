n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

max_tmp = [a[0]]
max_tmp.append([0, 0, 0])
min_tmp = [a[0]]
min_tmp.append([0, 0, 0])
for i in range(1, n):
    max_tmp[1][0] = max(max_tmp[0][0], max_tmp[0][1]) + a[i][0]
    max_tmp[1][1] = max(max_tmp[0][0], max_tmp[0][1], max_tmp[0][2]) + a[i][1]
    max_tmp[1][2] = max(max_tmp[0][2], max_tmp[0][1]) + a[i][2]
    max_tmp[0] = max_tmp[1][:]

    min_tmp[1][0] = min(min_tmp[0][0], min_tmp[0][1]) + a[i][0]
    min_tmp[1][1] = min(min_tmp[0][0], min_tmp[0][1], min_tmp[0][2]) + a[i][1]
    min_tmp[1][2] = min(min_tmp[0][2], min_tmp[0][1]) + a[i][2]
    min_tmp[0] = min_tmp[1][:]

print(max(max_tmp[0]), min(min_tmp[0]))