moem = ["A", "E", "I", "O", "U"]
cnt = -1
ans = 0


def func(res, word):
    global cnt, ans

    if len(res) > 5:
        return

    cnt += 1
    if res == word:
        ans = cnt
        return

    for x in moem:
        func(res + x, word)


def solution(word):
    func("", word)
    return ans