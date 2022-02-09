n = int(input())
s = input()

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(n)]

for i in range(n):
    if s[i] == "E":
        union(i, i + 1)
    else:
        union(i, i - 1)

res = []
for i in range(n):
    tmp = find(i)
    if tmp not in res:
        res.append(tmp)
print(len(res))

