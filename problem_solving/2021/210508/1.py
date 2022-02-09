def solution(s):
    answer = []
    s = list(s)
    tmp_list = []
    tmp = ""
    for x in s:
        if x.isdigit():
            if len(tmp) != 0:
                tmp_list.append(tmp)
            tmp_list.append(x)
            tmp = ""
        else:
            tmp += x
    tmp_list.append(tmp)

    num = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    for x in tmp_list:
        if x == "":
            continue

        if x.isdigit():
            answer.append(int(x))
        else:
            if x in num.keys():
                answer.append(num[x])
            else:
                i = 0
                for j in range(1, len(x)):
                    if x[i:j] in num.keys():
                        answer.append(num[x[i:j]])
                        i = j
                answer.append(num[x[i:]])

    return int("".join(map(str, answer)))

