def solution(student, k):
    ans = 0
    cnt = [0, 0]
    for lt in range(len(student)):
        rt = lt
        cnt = [0, 0]
        while rt < len(student):
            cnt[student[rt]] += 1
            if cnt[1] == k:
                ans += 1
            rt += 1
        cnt[student[lt]] -= 1
    return ans

solution([0, 1, 0, 0, 1, 1, 0], 2)
