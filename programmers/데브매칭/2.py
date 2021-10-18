from itertools import combinations


def solution(leave, day, holidays):
    if leave + len(holidays) >= 30:
        return 30

    cal = [""]
    day_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    s = day_list.index(day)
    for _ in range(30):
        cal.append(day_list[s])
        s = (s + 1) % 7

    a = [False] * 31
    tmp = []
    for i in range(1, 31):
        if i in holidays:
            a[i] = True
        if cal[i] in ["SAT", "SUN"]:
            a[i] = True

        if i not in holidays and cal[i] not in ["SAT", "SUN"]:
            tmp.append(i)

    c = list(combinations(tmp, leave))
    ans = 0
    for hol_comb in c:
        b = a[:]
        for x in hol_comb:
            b[x] = True

        for i in range(1, 31):
            cnt = 0
            if b[i]:
                for j in range(i, 31):
                    if not b[j]:
                        break
                    cnt += 1
            ans = max(ans, cnt)

    return ans

solution(0, "SUN", [])