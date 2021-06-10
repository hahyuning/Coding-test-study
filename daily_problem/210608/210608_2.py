n, k = map(int, input().split())
m = n - k
a = list(map(int, list(input())))
stack = []
for i in range(n):
    while stack and stack[-1] < a[i]:
        if k == 0:
            break

        stack.pop()
        k -= 1

    stack.append(a[i])

print("".join(map(str, stack[:n - m])))