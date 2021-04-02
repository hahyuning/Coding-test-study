def solution(n):
    samjinsu = ""
    while n > 0:
        a, b = divmod(n, 3)
        samjinsu += str(b)
        n = a

    answer = 0
    i = 0
    while len(samjinsu) > 0:
        answer += int(samjinsu[-1]) * (3 ** i)
        samjinsu = samjinsu[:-1]
        i += 1

    return answer

print(solution(45))

