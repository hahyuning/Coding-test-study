def check(a, b, inequality):
    if inequality == ">":
        if a > b:
            return True
    else:
        if a < b:
            return True
    return False

def permutation(index, num):
    # n + 1 개의 문자를 사용한 경우
    if index == n + 1:
        ans.append(num)
        return

    for i in range(10):
        # 백트래킹
        if check_list[i]:
            continue

        # index의 문자가 부등호를 만족하는지를 바로 체크
        if index == 0 or check(num[-1], str(i), inequalities[index - 1]):
            check_list[i] = True
            permutation(index + 1, num + str(i))
            check_list[i] = False

n = int(input())
inequalities = list(input().split())
ans = []
# 숫자 사용 여부 기록
check_list = [False] * 10

permutation(0, "")
print(ans[-1])
print(ans[0])
