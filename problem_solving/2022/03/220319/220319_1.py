def solution(logs):
    ans = 0
    keys = ["team_name", "application_name", "error_level", "message"]

    for log in logs:
        s_list = log.split()
        check = False
        if len(s_list) != 9:
            check = True
        else:
            for x in keys:
                if x not in s_list:
                    check = True
                    break
            else:
                for x in s_list:
                    if x not in keys and x != ":":
                        if len(x) > 100:
                            check = True
                            break
                        for x in log:
                            if x.isdigit():
                                check = True
                                break

        if check:
            print(log)
            ans += 1
    return ans

print(solution(["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]))