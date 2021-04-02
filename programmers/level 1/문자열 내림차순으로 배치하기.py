def solution(s):
    arr1 = []
    arr2 = []
    for x in s:
        if x.isupper():
            arr2.append(x)
        else:
            arr1.append(x)
    arr1 = sorted(arr1, reverse=True)
    arr2 = sorted(arr2, reverse=True)

    answer = arr1 + arr2
    return "".join(answer)