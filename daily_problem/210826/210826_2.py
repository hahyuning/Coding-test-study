def dfs(idx, s, plus, minus, mul, div):
    if idx == n:
        tmp = int(eval(s))
        ans.append(tmp)
        return

    if plus > 0:
        dfs(idx + 1, s + "+" + str(a[idx]), plus - 1, minus, mul, div)
    if minus > 0:
        dfs(idx + 1, s + "-" + str(a[idx]), plus, minus - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, s + "*" + str(a[idx]), plus, minus, mul - 1, div)
    if div > 0:
        dfs(idx + 1, s + "//" + str(a[idx]), plus, minus, mul, div - 1)

n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
ans = []
dfs(1, str(a[0]), plus, minus, mul, div)
print(max(ans))
print(min(ans))