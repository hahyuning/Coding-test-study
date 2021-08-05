while True:
    n, k = map(int, input().split())
    if n == 0:
        break

    num = list(map(int, input().split()))
    if k == num[0]:
        print(0)
        continue

    k_idx = num.index(k)
    parent = dict()
    parent[0] = -1
    pnt = -1
    for i in range(1, n):
        if num[i - 1] + 1 != num[i]:
            pnt += 1
        parent[i] = pnt

    ans = 0
    for i in range(1, n):
        if parent[i] != parent[k_idx] and parent[parent[i]] == parent[parent[k_idx]]:
            ans += 1
    print(ans)