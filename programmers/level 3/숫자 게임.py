import bisect

def solution(a, b):
    answer = 0
    a = [-x for x in a]
    b = [-x for x in b]
    a.sort()
    b.sort()

    for x in a:
        j = bisect.bisect_left(b, x)
        if j == 0:
            b.pop()
            continue

        b.remove(b[j - 1])
        answer += 1
    return answer

print(solution([5,1,3,7], [2,2,6,8]))