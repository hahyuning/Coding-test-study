def dfs(index, sum):
    global result

    if index == n:
        result[sum] = True
        return

    dfs(index + 1, sum + a[index])
    dfs(index + 1, sum)


n = int(input())
a = list(map(int, input().split()))
result = [False] * 2000000

dfs(0, 0)

for i in range(2000000):
    if not result[i + 1]:
        print(i + 1)
        break

