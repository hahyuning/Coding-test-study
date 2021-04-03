def solution(n):
    answer = 0
    a1 = 1
    a2 = 2
    if n == 1:
        return a1
    if n == 2:
        return a2
    for i in range(3, n + 1):
        answer = (a1 + a2) % 1234567
        a1 = a2
        a2 = answer
    return answer