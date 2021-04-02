import math, itertools

def is_prime_number(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    permutation_list = []
    for i in range(1,len(numbers) + 1):
        permutation_list += list(itertools.permutations(numbers, i))

    for p in permutation_list:
        p = int("".join(p))
        if is_prime_number(p):
            answer.add(p)
    return len(answer)

solution("011")