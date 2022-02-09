n, k = map(int, input().split())
order = list(map(int, input().split()))
ans = 0

multitab = []
for i, x in enumerate(order):
    if x in multitab:
        continue

    if len(multitab) < n:
        multitab.append(x)
    else:
        ans += 1
        late_order = -1
        late_item = -1
        for j, y in enumerate(multitab):
            if y not in order[i + 1:]:
                late_item = y
                break

            if late_order < order[i + 1:].index(y):
                late_order = order[i + 1:].index(y)
                late_item = y

        multitab[multitab.index(late_item)] = x

print(ans)
