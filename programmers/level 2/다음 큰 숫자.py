def solution(n):
    m = n
    while True:
        m += 1
        if count(n) == count(m):
            break
    return m

def count(num):
    cnt = 0
    bin_num = ""
    while num > 0:
        n, d = divmod(num, 2)
        bin_num += str(d)
        num = n

    for x in bin_num:
        if x == "1":
            cnt += 1
    return cnt

solution(78)