def solve(idx):
    global ans

    if sum(res) == n * (n + 1):
        ans += 1
        return

    if idx >= 2 * n + 1:
        return

    if res[idx] != 0:
        solve(idx + 1)

    for i in range(1, n + 1):
        if idx + i + 1 >= 2 * n + 1:
            break

        if not check[i]:
            if res[idx] == res[idx + i + 1] == 0:
                res[idx] = res[idx + i + 1] = i
                check[i] = True
                solve(idx + 1)
                res[idx] = res[idx + i + 1] = 0
                check[i] = False


n, x, y = map(int, input().split())
diff = y - x - 1

res = [0] * (2 * n + 1)
res[x] = res[y] = diff
check = [False] * (n + 1)
check[diff] = True

ans = 0
solve(1)
print(ans)