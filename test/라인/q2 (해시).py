from collections import Counter, defaultdict

def solution(research, n, k):
    ans = defaultdict(int)

    for i in range(len(research)):
        research[i] = Counter(list(research[i]))

    for i, day in enumerate(research):
        if i + n > len(research):
            break

        for key, val in day.items():
            if val >= k:
                cnt = 0

                for j in range(i, i + n):
                    if key not in research[j]:
                        break

                    if research[j][key] < k:
                        break

                    cnt += research[j][key]
                else:
                    if cnt >= 2 * n * k:
                        ans[key] += 1

    if len(ans.keys()) == 0:
        return "None"

    max_val = 0
    for key, val in ans.items():
        if val > max_val:
            max_val = val

    res = []
    for key, val in ans.items():
        if val == max_val:
            res.append(key)
    res.sort()

    return res[0]

solution(["yxxy", "xxyyy"], 2, 1)