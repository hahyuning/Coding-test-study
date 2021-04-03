def solution(n, s):
    if n > s:
        return [-1]

    i, j = divmod(s, n)
    answer = [i] * n
    for i in range(j):
        answer[i] += 1
    answer.sort()
    return answer