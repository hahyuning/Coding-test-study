def solution(seconds):
    snack = [[300, 10], [130, 30], [120, 20], [20, 30]]

    ans = 0
    for time, x in snack:
        cnt = 0
        while time * (cnt + 1) <= seconds and cnt + 1 <= x:
            cnt += 1
        seconds -= time * cnt
        ans += cnt

    return ans

solution(450)