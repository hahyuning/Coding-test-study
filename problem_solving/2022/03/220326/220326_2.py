from itertools import combinations

def solution(sentences, n):
    score = 0
    key_list = combinations([i for i in range(26)], n)
    for key in key_list:
        tmp = 0
        for s in sentences:
            check = False
            for x in s:
                if x == " ":
                    continue

                if x.isupper():
                    check = True
                    break

                num = ord(x) - ord("a")
                if num not in key:
                    check = True
                    break

            if not check:
                tmp += len(s)
        score = max(score, tmp)

    shift_key_list = combinations([i for i in range(26)], n - 1)
    for key in shift_key_list:
        tmp = 0
        for s in sentences:
            check = False
            cnt = 0
            for x in s:
                if x == " ":
                    continue

                if x.isupper():
                    cnt += 1
                    x = x.lower()

                num = ord(x) - ord("a")
                if not num in key:
                    check = True
                    break

            if not check:
                tmp += (len(s) + cnt)

        score = max(score, tmp)
    print(score)
    return score

solution(["line in line", "LINE", "in lion"], 5)