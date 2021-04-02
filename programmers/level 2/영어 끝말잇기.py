from collections import deque
def solution(n, words):
    answer = 1
    words_len = len(words)
    words = deque(words)
    check = []

    while words:
        w = words.popleft()
        if not check:
            check.append(w)
        elif check[-1][-1] == w[0] and w not in check:
            check.append(w)
        else:
            break
        answer += 1

    if not words and answer == words_len + 1:
        return [0, 0]
    return [answer % n if answer % n != 0 else n, answer // n  + 1 if answer % n != 0 else answer // n]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))