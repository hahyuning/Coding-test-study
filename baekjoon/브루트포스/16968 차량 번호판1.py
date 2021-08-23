# 재귀
def solution(idx, last):
    if len(s) == idx:
        return 1

    if s[idx] == "c":
        start = ord("a")
    else:
        start = ord("0")
    if s[idx] == "c":
        end = ord("z")
    else:
        end = ord("9")

    ans = 0
    for i in range(start, end + 1):
        if i != last:
            ans += solution(idx + 1, i)
    return ans

s = input()
print(solution(0, " "))