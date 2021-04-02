def solution(n):
    answer = ""
    while n > 0:
        n -= 1
        a, b = divmod(n, 3)
        answer += "124"[b]
        n = a
    return answer[::-1]

print(solution(10))
