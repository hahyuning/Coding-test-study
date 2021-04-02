def solution(nums):
    n = len(set(nums))
    if n <= len(nums) // 2:
        return n
    else:
        return len(nums) // 2