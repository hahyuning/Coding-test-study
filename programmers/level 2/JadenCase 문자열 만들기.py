def solution(s):
    s_list = list(s)
    for i, x in enumerate(s_list):
        if i == 0:
            if x.isalpha():
                s_list[i] = x.upper()
            continue

        if s_list[i - 1] == " " and x.isalpha():
            s_list[i] = x.upper()
        elif x != " " and x.isalpha():
            s_list[i] = x.lower()

    return "".join(s_list)

print(solution("3people unFollowed me"	))
