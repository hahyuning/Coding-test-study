def recursion(left, right):
    if left == right:
        return

    min_val = min(s[left:right])
    min_idx = s[left:right].index(min_val) + left

    check[min_idx] = True
    for i in range(n):
        if check[i]:
            print(s[i], end="")
    print()

    recursion(min_idx + 1, right)
    recursion(left, min_idx)

s = list(input())
n = len(s)
check = [False] * n
recursion(0, n)