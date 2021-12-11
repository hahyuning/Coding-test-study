def solution(n):
    k = n ** 2
    return 2 * k - 1 + 2 * (k - 1) - 1 + 2 * (k - 2) - 1

print(solution(4))