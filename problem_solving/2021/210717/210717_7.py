def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 1:
        return 1 - solution(n // 2)
    return solution(n // 2)

k = int(input())
print(solution(k - 1))