# 진법 변환 메서드
def base_change(num, base):
    T = "0123456789ABCDEF"

    n, d = divmod(num, base)
    if n == 0:
        return [T[d]]

    return base_change(n, base) + [T[d]]

def solution(n, t, m, p):
    # n: 진법, t: 미리 구할 갯수, m: 참가 인원, p: 튜브의 순서

    ans = ""
    num = 0
    all = []

    while len(all) < t * m:
        all += base_change(num, n)
        num += 1

    for i in range(t * m):
        # 튜브의 차례인 경우
        if i % m == p - 1:
            ans += all[i]

    return ans