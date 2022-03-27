from collections import defaultdict

def solution(num_teams, remote_tasks, office_tasks, employees):
    ans = []
    team_members = defaultdict(list)
    office_members = defaultdict(list)

    for i in range(1, len(employees) + 1):
        num, *tasks = employees[i - 1].split()
        num = int(num)
        team_members[num].append(i)

        office_check = False
        for x in tasks:
            if x in office_tasks:
                office_check = True
                break

        if office_check:
            office_members[num].append(i)

    for i in range(1, num_teams + 1):
        if i in office_members:
            ans += office_members[i]
        else:
            team_members[i].sort()
            ans.append(team_members[i][0])

    return [i for i in range(1, len(employees) + 1) if i not in ans]

print(solution(3, ["development", "marketing", "hometask"], ["recruitment", "education", "officetask"], ["1 development hometask", "1 recruitment marketing", "2 hometask", "2 development marketing hometask", "3 marketing", "3 officetask", "3 development"]))