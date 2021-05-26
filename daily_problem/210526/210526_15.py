s = list(input())
proper = []

stack = []
for i, x in enumerate(s):
    if x == "(":
        stack.append((x, i))
    elif x == ")":
        y, j = stack.pop()
        proper.append((j, i))

k = len(proper)
ans = []
for i in range(1 << k):
    tmp = []
    for j in range(k):
        if i & (1 << j):
            tmp.append(proper[j][0])
            tmp.append(proper[j][1])

    new_word = ""
    for j, x in enumerate(s):
        if j not in tmp:
            new_word += x
    ans.append(new_word)

ans = ans[1:]
ans = set(ans)
ans = sorted(ans)
for x in ans:
    print(x)
