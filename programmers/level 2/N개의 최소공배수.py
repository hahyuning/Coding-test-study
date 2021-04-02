from math import gcd

def lmc(x, y):
    return x * y // gcd(x, y)

def solution(arr):
    while len(arr) > 1:
        a = arr.pop()
        b = arr.pop()
        arr.append(lmc(a, b))
    return arr[0]