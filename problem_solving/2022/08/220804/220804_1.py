from collections import Counter

def solution(X, Y):
    x_list = Counter(X)
    y_list = Counter(Y)

    common = []
    for k in x_list.keys():
        if k in y_list:
            for i in range(min(x_list[k], y_list[k])):
                common.append(k)

    if not common:
        return "-1"

    if set(common) == {"0"}:
        return "0"

    common.sort(reverse=True)
    return "".join(common)

print(solution("100", "203045"))