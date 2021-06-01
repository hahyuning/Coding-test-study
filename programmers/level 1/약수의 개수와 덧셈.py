def division(x):
    # true: 짝수, false: 홀수
    ans = True
    cnt = 0
    for y in range(1, x + 1):
        if x % y == 0:
            cnt += 1

    if cnt % 2 != 0:
        ans = False
    return ans

def solution(left, right):
    answer = 0
    for x in range(left, right + 1):
        res = division(x)
        print(x, res)
        if res:
            answer += x
        else:
            answer -= x
    return answer

print(solution(13, 17))