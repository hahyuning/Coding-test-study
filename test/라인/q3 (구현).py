def solution(jobs):
    ans = []
    # 저장정보 = 분류번호: [중요도의 합, 걸리는 시간]
    wait = dict()

    now = jobs[0][2]
    end = jobs[0][0] + jobs[0][1]
    check = [False] * len(jobs)
    check[0] = True

    while True:
        if not ans:
            ans.append(now)
        else:
            if ans[-1] != now:
                ans.append(now)

        same_num = False
        for i, job in enumerate(jobs):
            if not check[i]:
                if job[0] <= end:
                    check[i] = True

                    if job[2] == now:
                        same_num = True

                    if job[2] in wait:
                        wait[job[2]][0] += job[3]
                        wait[job[2]][1] += job[1]
                    else:
                        wait[job[2]] = [job[3], job[1]]

        if same_num or now in wait:
            end += wait[now][1]
            del wait[now]
            continue

        if len(wait) == 0:
            for i in range(len(jobs)):
                if not check[i]:
                    check[i] = True
                    now = jobs[i][2]
                    end += jobs[i][1]
                    break
            else:
                break
            continue

        max_priority = 0
        for num in wait:
            p, t = wait[num]
            max_priority = max(max_priority, p)

        tmp = []
        for num in wait:
            p, t = wait[num]
            if p == max_priority:
                tmp.append((num, t))
        tmp.sort()

        now = tmp[0][0]
        end += tmp[0][1]
        del wait[now]

    return ans

solution([[0, 2, 3, 1], [5, 3, 3, 1], [10, 2, 4, 1]])