def solution(k):
    if k == 0:
        return "-"

    return solution(k - 1) + " " * (3 ** (k - 1)) + solution(k - 1)

while True:
    try:
        n = int(input())
        print(solution(n))
    except:
        break