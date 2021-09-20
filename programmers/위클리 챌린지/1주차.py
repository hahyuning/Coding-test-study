def solution(price, money, count):
    need = 0
    for i in range(count + 1):
        need += price * i

    if money >= need:
        return 0
    return need - money