from bisect import bisect_right, bisect_left
from collections import defaultdict

def solution(registered_list, new_id):
    registered_dict = defaultdict(list)
    for x in registered_list:
        idx = -1
        for i in range(len(x)):
            if x[i].isdigit():
                idx = i
                break
        if idx == -1:
            n = x
            s = 0
        else:
            n = x[:idx]
            s = int(x[idx:])
        registered_dict[n].append(s)

    for val in registered_dict.values():
        val.sort()

    ans = ""
    idx = -1
    for i in range(len(new_id)):
        if new_id[i].isdigit():
            idx = i
            break
    if idx == -1:
        n = new_id
        s = 0
    else:
        n = new_id[:idx]
        s = int(new_id[idx:])

    tmp = registered_dict[n]
    if not tmp:
        if s == 0:
            ans = n
        else:
            ans = n + str(s)
    else:
        idx = bisect_right(tmp, s)
        if idx == 0:
            if s == 0:
                ans = n
            else:
                ans = n + str(n)
        else:
            while True:
                idx = bisect_right(tmp, s)
                if tmp[idx - 1] != s:
                    ans = n + str(s)
                    break
                s += 1

    return ans


print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "asdf11"))