def dfs(e):
    global maxVal
    if len(energy) == 2:
        maxVal = max(maxVal, e)
        return

    for i in range(1, len(energy) - 1):
        w = energy[i - 1] * energy[i + 1]
        tmp = energy[i]

        del energy[i]
        dfs(e + w)
        energy.insert(i, tmp)

n = int(input())
energy = list(map(int, input().split()))

maxVal = 0
dfs(0)
print(maxVal)