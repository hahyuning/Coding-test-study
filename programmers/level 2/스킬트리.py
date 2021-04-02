def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    for skills in skill_trees:
        s_pnt = 0
        for s in skills:
            if s in skill:
                if s_pnt < skill.index(s):
                    break
                s_pnt += 1
        else:
            answer += 1
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))