def solution(n):
    answer = 0
    a = 1
    b = 2
    for _ in range(n - 2):
        answer = (a + b) % 1000000007
        a = b
        b = answer
    return answer