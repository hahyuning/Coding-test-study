n = int(input())

for _ in range(n):
    str = input()
    count = 0 # 0 아래로 내려가면 올바른 괄호 문자열이 아님
    x = 0
    while x < len(str):
        if str[x] == '(':
            count += 1

        elif str[x] == ')':
            if count == 0:
                print("NO")
                break
            count -= 1
        x += 1

    # 끝까지 검사를 마쳤고 괄호쌍이 맞는 경우
    if x == len(str) and count == 0:
        print("YES")
    # 끝까지 검사를 마쳤으나 괄호쌍이 맞지 않는 경우
    elif x == len(str) and count != 0:
        print("NO")

