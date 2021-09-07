def solution(files):
    ans = []

    cnt = 0
    for file in files:
        s, e = -1, -1
        for i, x in enumerate(file):
            if x.isdigit():
                if s == -1:
                    s = i
                e = i
            else:
                if e != -1:
                    break
        ans.append((file[:s], file[s:e + 1], file[e + 1:], cnt))
        cnt += 1

    ans.sort(key=lambda x:(x[0].lower(), int(x[1]), x[3]))
    ans = ["".join(x[:-1]) for x in ans]

    return ans

