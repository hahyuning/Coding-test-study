import re
from collections import Counter

def multi_list(str):
    # 영어 소문자 두번 반복
    r = re.compile("[a-z]{2}")

    res = []
    for i in range(len(str) - 1):
        tmp = str[i:i + 2]
        if r.match(tmp):
            res.append(tmp)
    return res

def solution(str1, str2):
    list1 = multi_list(str1.lower())
    list2 = multi_list(str2.lower())

    n = len(list1)
    m = len(list2)

    # 두 집합이 모두 공집합인 경우
    if n == 0 and m == 0:
        return 65536

    set1 = Counter(list1)
    set2 = Counter(list2)

    # 교집합
    # 두 카운터에 모두 포함되는 원소: 그 중 작은 값
    intersection = set1 & set2
    # 카운터 역연산
    intersection = list(intersection.elements())
    x = len(intersection)

    return int((x / (n + m - x)) * 65536)

solution("handshake", "shake hands")
