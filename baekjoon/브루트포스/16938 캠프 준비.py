def recursion(i, b, start):
    global ans
    if len(b) == i:
        if backtracking(b):
            ans += 1
        return

    if start >= n:
        return

    for j in range(start, n):
        if check[j]:
            check[j] = False
            recursion(i, b + [a[j]], j + 1)
            check[j] = True

def backtracking(b):
    if len(b) < 2:
        return True

    b.sort()
    if l <= sum(b) <= r and b[-1] - b[0] >= x:
        return True
    return False

n, l, r, x = map(int, input().split())
# 가장 어려운 문제 - 가장 쉬운 문제 >= x

a = list(map(int, input().split()))
check = [True] * n
ans = 0
for i in range(2, n + 1):
    recursion(i, [], 0)
print(ans)