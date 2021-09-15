from collections import defaultdict

def solution(id_list, report, k):
    n = len(id_list)
    ans = [0] * n

    name = defaultdict(list)
    cnt = defaultdict(int)
    report = list(set(report))
    for x in report:
        a, b = x.split(" ")
        cnt[b] += 1
        name[a].append(b)

    res = []
    for key, val in cnt.items():
        if val >= k:
            res.append(key)

    for i in range(n):
        if id_list[i] in name.keys():
            tmp = 0
            for x in name[id_list[i]]:
                if x in res:
                    tmp += 1
            ans[i] = tmp

    return ans

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)