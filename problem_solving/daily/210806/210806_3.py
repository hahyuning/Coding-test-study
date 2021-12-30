m = int(input())
ans = [i for i in range(4)]

for _ in range(m):
    a, b = map(int, input().split())
    x = ans.index(a)
    y = ans.index(b)
    ans[x], ans[y] = ans[y], ans[x]
print(ans[1])