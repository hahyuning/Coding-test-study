def solution(n):
    ans = []

    def move(fr, to, mid, n):
        nonlocal ans
        if n == 1:
            ans.append([fr, to])
            return

        move(fr, mid, to, n - 1)
        ans.append([fr, to])
        move(mid, to, fr, n - 1)

    move(1, 3, 2, n)
    return ans