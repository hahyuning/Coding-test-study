ans = -1
visited = []


def check(s, cnt):
    global ans
    if "1" not in s:
        if ans == -1 or cnt < ans:
            ans = cnt
        return

    visited.append(s)
    if s[-1] == "1":
        tmp = s[:-1] + "0"
        if tmp not in visited:
            check(tmp, cnt + 1)
    else:
        tmp = s[:-1] + "1"
        if tmp not in visited:
            check(tmp, cnt + 1)

    for i in range(len(s) - 1):
        if s[i + 1] == "1":
            if i + 1 == len(s) - 1 or "1" not in s[i + 2:]:
                if s[i] == "1":
                    tmp = s[:i] + "0" + s[i + 1:]
                    if tmp not in visited:
                        check(tmp, cnt + 1)
                else:
                    tmp = s[:i] + "1" + s[i + 1:]
                    if tmp not in visited:
                        check(tmp, cnt + 1)


def minOperations(n):
    num = bin(n)[2:]
    check(num, 0)
    return ans

print(minOperations(10 ** 15))