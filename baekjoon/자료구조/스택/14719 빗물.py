n, m = map(int, input().split())
rains = list(map(int, input().split()))

max_index = rains.index(max(rains))

res = 0
tmp = 0
for i in range(0, max_index + 1):
    if rains[i] > tmp:
        tmp = rains[i]
    res += tmp

tmp = 0
for j in range(m - 1, max_index, -1):
    if rains[j] > tmp:
        tmp = rains[j]
    res += tmp

print(res - sum(rains))