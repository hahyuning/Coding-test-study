def permutation(index):
    if index == m:
        res.add(" ".join(map(str, ans)))
        return
    for i in range(n):
        if check[i]:
            continue

        check[i] = True
        ans[index] = a[i]
        permutation(index + 1)
        check[i] = False

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

ans = [0] * m
check = [False] * n
res = set()
permutation(0)

for x in res:
    print(x)