from itertools import combinations
from copy import deepcopy

def solution(abilities, k):
    ans = 0
    n = len(abilities)
    c_list = combinations([i for i in range((n + 1) // 2)], k)
    abilities.sort()

    for c in c_list:
        score = 0
        tmp = deepcopy(abilities)
        for i in range((n + 1) // 2):
            if i == (n + 1) // 2 - 1:
                if len(tmp) == 1:
                    if i in c:
                        score += tmp[-1]
                else:
                    if i in c:
                        score += tmp[-1]
                    else:
                        score += tmp[0]
            else:
                if i in c:
                    score += tmp.pop()
                    tmp.pop()
                else:
                    tmp.pop()
                    score += tmp.pop()

        ans = max(ans, score)

    return ans

solution([7, 6, 8, 9, 10], 1)