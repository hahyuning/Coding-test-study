# 만들어진 문자열이 조건을 만족하는지 확인
def check(string):
    jaum = 0
    moum = 0

    for s in string:
        if s == "a" or s == "e" or s == "i" or s == "o" or s == "u":
            moum += 1
        else:
            jaum += 1

    if moum >= 1 and jaum >= 2:
        return True
    else:
        return False

# 가능한 조합 만들기
def combination(index, password):
    # 종료 조건: 비밀번호의 길이가 m인 경우
    if len(password) == m:
        if check(password):
            print(password)
        return

    # 종료 조건: 비밀번호의 길이가 m보다 짧지만 인덱스 범위 초과
    if index >= n:
        return

    combination(index + 1, password + char_list[index])
    combination(index + 1, password)

# ----------------------------------------------------
m, n = map(int, input().split())
char_list = input().split()
char_list.sort()

combination(0, "")