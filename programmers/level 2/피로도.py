from itertools import permutations

def move(k, p, dungeons):
    cnt = 0
    for i in p:
        i -= 1
        need = dungeons[i][0]
        consume = dungeons[i][1]
        if k >= need:
            cnt += 1
            k -= consume
        else:
            return cnt
    return cnt

def solution(k, dungeons):
    ans = -1
    n = len(dungeons)
    p_list = list(permutations([i for i in range(1, n + 1)]))

    for p in p_list:
        ans = max(ans, move(k, p, dungeons))
    return ans

print(solution(80, [[80,20],[50,40],[30,10]]))