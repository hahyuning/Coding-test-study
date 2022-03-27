def solution(logs):
    ans = 0
    keys = ["team_name", "application_name", "error_level", "message"]

    for log in logs:
        check = False
        if "  " in log or len(log) > 100:
            check = True
        else:
            s_list = log.split(" ")
            if len(s_list) != 12:
                check = True
            else:
                for x in keys:
                    if x not in s_list:
                        check = True
                        break
                else:
                    cnt = 0
                    for x in s_list:
                        if x == ":":
                            cnt += 1
                            continue

                        if x not in keys:
                            for y in x:
                                if not y.isalpha():
                                    check = True
                                    break

                    if cnt != 4:
                        check = True
        if check:
            ans += 1
    return ans
