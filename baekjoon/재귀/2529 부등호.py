n = int(input())
inequalities = list(input().split())
ans = []
check_list = [False] * 10

def check(a, b, inequality):
    if inequality == ">":
        if a > b:
            return True
    else:
        if a < b:
            return True
    return False

def permutation(index, num):
    if index == n + 1:
        ans.append(num)
        return

    for i in range(10):
        if check_list[i]:
            continue

        if index == 0 or check(num[-1], str(i), inequalities[index - 1]):
            check_list[i] = True
            permutation(index + 1, num + str(i))
            check_list[i] = False

permutation(0, "")
print(ans[-1])
print(ans[0])
