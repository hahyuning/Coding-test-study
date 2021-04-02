import math
def solution(n):
    answer = 0
    sqr_num = math.sqrt(n)
    if sqr_num == int(sqr_num):
        return (sqr_num + 1) ** 2
    else:
        return -1
