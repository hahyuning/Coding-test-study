def gcd(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // (gcd(a, b))

def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    return answer