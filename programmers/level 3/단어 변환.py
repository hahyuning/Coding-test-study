from collections import deque

# 단어가 하나만 차이나는지 확인
def diff_one(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1

    if cnt == 1:
        return True
    return False

def solution(begin, target, words):

    q = deque()
    visited = dict()

    q.append((begin, 0))
    visited[begin] = True

    answer = 0
    while q:
        now, cost = q.popleft()
        for word in words:
            # 두 원소가 한 글자 차이나고 방문한 적이 없다면
            if diff_one(word, now) and word not in visited:
                q.append((word, cost + 1))
                visited[word] = True

                if word == target:
                    answer = cost + 1
                    break
    return answer