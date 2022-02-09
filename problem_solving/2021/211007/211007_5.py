def find(i):
    if i == 0:
        return 1

    if i in d:
        return d[i]

    d[i] = find(i // p) + find(i // q)
    return d[i]

n, p, q = map(int, input().split())
d = dict()
print(find(n))