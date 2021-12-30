def solution(numArr):
    s = sum(numArr)
    e = s / 3
    grade = ""

    if 90 <= e:
        grade = "A"
    elif 80 <= e:
        grade = "B"
    elif 70 <= e:
        grade = "C"
    elif 60 <= e:
        grade = "D"
    else:
        grade = "F"
    return ["{:.3f}".format(e), grade]

solution([100, 100, 98])