def solution(gems):
    n = len(set(gems))
    left = 0
    right = 0

    ans = [0, len(gems)]
    check = {gems[0]:1}
    while left < len(gems) and right < len(gems):
        if len(check) == n:
            if ans[1] - ans[0] > right - left:
                ans = [left + 1, right + 1]

            if check.get(gems[left]) == 1:
                del check[gems[left]]
            else:
                check[gems[left]] = max(0, check.get(gems[left], 0) - 1)
            left += 1

        else:
            right += 1
            if right < len(gems):
                check[gems[right]] = check.get(gems[right], 0) + 1

    print(ans)

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])