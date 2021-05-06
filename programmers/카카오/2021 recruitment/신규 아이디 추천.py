def solution(new_id):
    special = ["-", "_", "."]
    step1 = []
    for x in new_id:
        if x.isupper():
            step1.append(x.lower())
        elif x.islower() or x.isdigit() or x in special:
            step1.append(x)

    step3 = []
    i = 0
    prev = 0
    while i < len(step1):
        if step1[i] == ".":
            cnt = 1
            for j in range(i + 1, len(step1)):
                if step1[j] == ".":
                    cnt += 1
                else:
                    break
            if cnt >= 2:
                step3 += step1[prev:i + 1]
            else:
                step3 += "."

            i += cnt
            prev = i
        else:
            step3 += step1[i:i + 1]
            i += 1
            prev = i

    step3 += step1[prev:]

    while step3 and step3[0] == ".":
        step3.pop(0)
    while step3 and step3[-1] == ".":
        step3.pop()

    if len(step3) == 0:
        step3.append("a")
    elif len(step3) > 15:
        step3 = step3[:15]

    while step3 and step3[-1] == ".":
        step3.pop()

    while len(step3) < 3:
        step3.append(step3[-1])

    return "".join(step3)

print(solution("...!@BaT#*..y.abcdefghijklm"))