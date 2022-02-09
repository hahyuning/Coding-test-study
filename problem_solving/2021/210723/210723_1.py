# 1: add
# 2: remove
# 3, 4: shift

n, m = map(int, input().split())
train = [0] * n
for _ in range(m):
    num, *a = map(int, input().split())
    if num == 1:
        i, x = a[0] - 1, a[1] - 1
        train[i] = (train[i] | (1 << x))
    elif num == 2:
        i, x = a[0] - 1, a[1] - 1
        train[i] = (train[i] & ~(1 << x))
    elif num == 3:
        i = a[0] - 1
        train[i] = train[i] << 1
        # 맨 앞자리 비우기
        train[i] = train[i] & ~(1 << 20)
    else:
        i = a[0] - 1
        train[i] = train[i] >> 1

print(len(set(train)))