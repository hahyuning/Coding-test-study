n = int(input())

lt = 1
rt = 1
s = 1
cnt = 0
while rt < n:
    if s < n:
        rt += 1
        s += rt
    elif s > n:
        s -= lt
        lt += 1
        if lt > rt:
            rt = lt
    else:
        cnt += 1
        lt += 1
        rt = lt
        s = lt
print(cnt + 1)