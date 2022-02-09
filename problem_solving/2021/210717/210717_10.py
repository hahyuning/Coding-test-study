def solution(x):
    if len(x) == 1:
        return True

    for i in range(len(x) // 2):
        if x[i] == x[len(x) - i - 1]:
            return False
    return solution(x[:len(x) // 2]) and solution(x[len(x) // 2 + 1:])

t = int(input())
for _ in range(t):
    s = input()
    if solution(s):
        print("YES")
    else:
        print("NO")