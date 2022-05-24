def solution(idx, s):
    global ans

    if s == "":
        tmp = 0
        for i in range(n):
            if check[i]:
                tmp += book[i][0]
        if ans == -1 or tmp < ans:
            ans = tmp
            return

    if idx >= n:
        return

    # idx 번째 책을 사지 않는 경우
    solution(idx + 1, s)

    # idx 번째 책을 사는 경우
    check[idx] = True
    ss = s
    for x in book[idx][1]:
        if x in ss:
            i = ss.index(x)
            ss = ss[:i] + ss[i + 1:]
    solution(idx + 1, ss)
    check[idx] = False


t = input()
n = int(input())

book = []
for _ in range(n):
    price, name = input().split()
    book.append((int(price), name))

check = [False] * n
ans = -1
solution(0, t)

print(ans)