def solution(idx, res):
    global ans
    if idx == 10:
        s = 0
        for i in range(10):
            if res[i] == a[i]:
                s += 1
        if s >= 5:
            ans += 1
        return

    for i in range(1, 6):
        if idx >= 2 and res[idx - 1] == res[idx - 2] == i:
            continue
        solution(idx + 1, res + [i])

a = list(map(int, input().split()))
ans = 0
solution(0, [])
print(ans)