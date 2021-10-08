from math import factorial


def solution(n, k):
    order = list(range(1, n + 1))
    answer = []

    while n != 0:
        fact = factorial(n - 1)
        answer.append(order.pop((k - 1) // fact))
        n -= 1
        k = k % fact
    return answer