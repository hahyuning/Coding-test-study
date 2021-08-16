def solution(position_list):
    po, pd, fe, be = 0, 0, 0, 0
    for x in position_list:
        if x == "PO":
            po += 1
        elif x == "PD":
            pd += 1
        elif x == "FE":
            fe += 1
        else:
            be += 1

    if po >= 3:
        return 0

    if po == 2:
        if pd > 1:
            return 0

        elif pd == 1:
            if fe > 2:
                return 0

            if fe == 2:
                return 1
            elif fe == 1:
                return 2

    if po == 1:
        if pd > 2:
            return 0
        elif pd == 1:
            if fe > 3:
                return 0

            if fe == 3:
                return 1
            elif fe == 2:
                return 3
            elif fe == 1:
                if be == 1:
                    return 2
                elif be >= 2:
                    return 3
    return 0

print(solution(["PO", "PD", "FE", "BE"]))
print(solution(["PO", "PD", "PO", "BE", "FE", "BE"]))
print(solution(["PO", "PD", "PO", "PD", "FE", "BE"]))
print(solution(["PO", "PD", "FE", "BE", "BE", "FE"]))