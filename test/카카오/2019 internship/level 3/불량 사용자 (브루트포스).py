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

def solution(user_ids, banned_ids):
    ans = []

    # 가능한 사용자 아이디의 쌍을 모두 만들고
    for candi_ids in permutations(user_ids, len(banned_ids)):
        # 해당 쌍이 불량 아이디와 매치되는지 확인
        if isMatch(candi_ids, banned_ids):
            tmp = set(candi_ids)
            if tmp not in ans:
                ans.append(tmp)

    return len(ans)