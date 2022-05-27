def count():
    res = 0
    for i in range(n - 1):
        if ans[i] == "A":
            for j in range(i + 1, n):
                if ans[j] == "B":
                    res += 1
    return res

n, k = map(int, input().split())

ans = ["B"] * n
for i in range(n):
    ans[i] = "A"
    if count() == k:
        break
    if count() > k:
        ans[i] = "B"

ans = "".join(ans)
if ans in ["A" * n, "B" * n]:
    if k == 0:
        print(ans)
    else:
        print(-1)
else:
    print(ans)