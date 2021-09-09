n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
partitions = []
p_size = min(n, m) // 2

# 파티션 나누기
for k in range(p_size):
    tmp = []
    # 윗변
    for j in range(k, m - k):
        tmp.append(a[k][j])
    # 오른변
    for i in range(k + 1, n - 1 - k):
        tmp.append(a[i][m - 1 - k])
    # 아랫변
    for j in range(m - 1 - k, k, -1):
        tmp.append(a[n - 1 - k][j])
    # 왼변
    for i in range(n - 1 - k, k, -1):
        tmp.append(a[i][k])
    partitions.append(tmp)

# 회전
for k in range(p_size):
    tmp = partitions[k]
    t_size = len(tmp)
    t_idx = r % t_size
    # 윗변
    for j in range(k, m - k):
        a[k][j] = tmp[t_idx]
        t_idx = (t_idx + 1) % t_size
    # 오른변
    for i in range(k + 1, n - 1 - k):
        a[i][m - 1 - k] = tmp[t_idx]
        t_idx = (t_idx + 1) % t_size
    # 아랫변
    for j in range(m - 1 - k, k, -1):
        a[n - 1 - k][j] = tmp[t_idx]
        t_idx = (t_idx + 1) % t_size
    # 왼변
    for i in range(n - 1 - k, k, -1):
        a[i][k] = tmp[t_idx]
        t_idx = (t_idx + 1) % t_size

for row in a:
    print(" ".join(map(str, row)))
