def solution(phone_number):
    n = len(phone_number)
    return "*" * (n - 4) + phone_number[n - 4:]