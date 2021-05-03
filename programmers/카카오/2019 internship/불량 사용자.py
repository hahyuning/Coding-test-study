from itertools import permutations

def isMatch(candi_ids, banned_ids):
    for i in range(len(candi_ids)):
        # 글자 길이가 다른 경우
        if len(candi_ids[i]) != len(banned_ids[i]):
            return False

        for j in range(len(candi_ids[i])):
            if banned_ids[i][j] == "*":
                continue
            if candi_ids[i][j] != banned_ids[i][j]:
                return False
    return True

def solution(user_ids, baaned_ids):
    ans = []
    for candi_ids in permutations(user_ids, len(baaned_ids)):
        if isMatch(candi_ids, baaned_ids):
            c_set = set(candi_ids)
            if c_set not in ans:
                ans.append(c_set)
    return len(ans)