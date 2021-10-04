def solve(res):
    global ans
    if len(res) == len(a):
        if a == res:
            ans = 1
        return

    # A 제거
    if res[-1] == "A":
        solve(res[:-1])
    # 뒤집고 B 제거
    tmp = res[::-1]
    if tmp[-1] == "B":
        solve(tmp[:-1])

a = input()
b = input()

ans = 0
solve(b)
print(ans)