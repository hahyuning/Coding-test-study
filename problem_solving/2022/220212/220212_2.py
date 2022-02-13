n, m = map(int, input().split())

connect = dict()
for i in range(1, n + 1):
    k, *num = map(int, input().split())
    connect[i] = num

for i in range(1, n + 1):
    check = [False] * (m + 1)
    for j in range(1, n + 1):
        if i == j:
            continue

        for x in connect[j]:
            check[x] = True

    if sum(check) == m:
        print(1)
        break
else:
    print(0)