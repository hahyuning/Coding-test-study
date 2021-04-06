def dfs(index, result):
    if len(result) == 6:
        print(" ".join(map(str, result)))
        return
    if index == len(a):
        return


    dfs(index + 1, result + [a[index]])
    dfs(index + 1, result)

while True:
    n, *a = list(map(int, input().split()))
    if n == 0:
        break

    dfs(0, [])
    print()

