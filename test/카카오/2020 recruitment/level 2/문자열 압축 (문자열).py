def solution(s):
    n = len(s)

    ans = n
    for size in range(1, n // 2 + 1):
        tmp = ""
        prev = s[:size]
        cnt = 1

        for i in range(size, n, size):
            if prev == s[i:i + size]:
                cnt += 1
            else:
                tmp += str(cnt) + prev if cnt >= 2 else prev
                prev = s[i:i + size]
                cnt = 1
        tmp += str(cnt) + prev if cnt >= 2 else prev
        ans = min(ans, len(tmp))

    return ans