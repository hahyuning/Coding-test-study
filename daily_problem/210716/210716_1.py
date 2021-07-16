def solution(idx, ss):
    global ans
    if idx == n:
        cnt = 0
        for x in ss:
            if x <= 0:
                cnt += 1
        ans = max(ans, cnt)
        return

    if ss[idx] > 0:
        check = False
        for i in range(n):
            if ss[i] > 0 and i != idx:
                check = True
                tmp = ss[:]
                tmp[i] -= w[idx]
                tmp[idx] -= w[i]
                solution(idx + 1, tmp)
        # 깰 계란이 없는 경우
        if not check:
            solution(idx + 1, ss)
    # 손에 든 계란이 깨져 있는 경우
    else:
        solution(idx + 1, ss)

n = int(input())
s = []
w = []
for _ in range(n):
    a, b = map(int, input().split())
    s.append(a)
    w.append(b)

ans = 0
solution(0, s)
print(ans)