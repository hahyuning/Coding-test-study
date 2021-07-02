def permutation(index, start):
    if index == m:
        res.add(" ".join(map(str, ans)))
        return

    if start >= n:
        return

    for i in range(start, n):
        ans[index] = a[i]
        permutation(index + 1, i)

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

ans = [0] * m
res = set()
permutation(0, 0)

for x in res:
    print(x)