def solution(s):
    cnt = 0
    bi_cnt = 0
    while s != "1":
        x, y = zero_delete(s)
        cnt += y

        s = binary(len(x))
        bi_cnt += 1
    return [bi_cnt, cnt]

# 2진수로 변환
def binary(num):
    ans = ""
    while num > 0:
        n, d = divmod(num, 2)
        ans += str(d)
        num = n
    return ans

# 0을 제거하고 난 후의 문자와 제거한 0의 갯수 반환
def zero_delete(s):
    res = ""
    cnt = 0
    for i in range(len(s)):
        if s[i] == "0":
            cnt += 1
        else:
            res += s[i]
    return [res, cnt]