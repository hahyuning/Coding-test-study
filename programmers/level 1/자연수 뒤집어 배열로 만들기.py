def solution(n):
    answer = list(map(int, str(n)))
    return answer[::-1]

print(solution(12345))