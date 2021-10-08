from collections import defaultdict

def solution(enroll, referral, seller, amount):
    ans = defaultdict(int)
    graph = dict()

    for i in range(len(enroll)):
        x = enroll[i]
        y = referral[i]

        if y == "-":
            graph[x] = "center"
        else:
            graph[x] = y

    for i in range(len(seller)):
        child = seller[i]
        money = amount[i] * 100
        while money > 0:
            parent = graph[child]
            tmp = money - money // 10
            ans[child] += tmp
            money -= tmp
            child = parent
            if child == "center":
                break

    res = []
    for x in enroll:
        res.append(ans[x])
    return res


solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10])