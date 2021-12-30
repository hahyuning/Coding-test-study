def solution(left, right, t, route):
    global ans
    if left <= 0 and right >= n - 1:
        if route not in check:
            check.append(route)
            ans += 1
        return

    if left == 0 and right < n - 1:
        tmp = t + s[right + 1]
        solution(left, right + 1, tmp, route + [tmp])
    elif right == n - 1 and left > 0:
        tmp = s[left - 1] + t
        solution(left - 1, right, tmp, route + [tmp])
    elif 0 < left and right < n - 1:
        tmp1 = t + s[right + 1]
        solution(left, right + 1, tmp1, route + [tmp1])
        tmp2 = s[left - 1] + t
        solution(left - 1, right, tmp2, route + [tmp2])

s = list(input())
n = len(s)
ans = 0
check = []
for i, x in enumerate(s):
    solution(i, i, x, [x])
print(ans)
