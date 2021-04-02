from itertools import combinations
import math

def solution(nums):
    cnt = 0
    for x in combinations(nums, 3):
        num = sum(x)
        if prime(num):
            cnt += 1
    return cnt

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True