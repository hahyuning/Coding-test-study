def solution(x):
    n_sum, n = 0, x

    while n >= 1:
        n_sum += n % 10
        n //= 10

    if x % n_sum == 0:
        return True
    return False