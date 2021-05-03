def solution(s):
    s = s[2:-2]
    a = s.split("},{")

    for i in range(len(a)):
        tmp = set(map(int, a[i].split(",")))
        a[i] = tmp
    a.sort(key=lambda x:len(x))

    ans = []
    prev = set()
    for i in range(len(a)):
        tmp = a[i]
        b = a[i] - prev
        for x in b:
            ans.append(x)
        prev = tmp

    return ans


solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
solution("{{20,111},{111}}")
solution("{{123}}")
solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")