def solution(n):
    answer = 0
    num = [i for i in range(1, (n + 1) // 2 + 1)]

    left, right = 0, 0
    while left < len(num) and right < len(num):
        if sum(num[left:right + 1]) < n:
            right += 1
        elif sum(num[left:right + 1]) > n:
            left += 1
        else:
            answer += 1
            left += 1
    return answer + 1