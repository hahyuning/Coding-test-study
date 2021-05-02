# start: 시작 단어, cnt: 배운 단어
def alphabet(start, cnt):
    global ans
    # 종료 조건: 배운 단어가 k개
    if cnt == k:
        # 읽을 수 있는 단어
        read_cnt = 0
        for word in words_set:
            for w in word:
                # 배울 수 없는 단어가 있는 경우
                if not learn[ord(w) - ord("a")]:
                    break
            else:
                read_cnt += 1
        # 정답 최대값으로 갱신
        ans = max(read_cnt, ans)
        return

    # 시작 단어부터 재귀 호출
    for i in range(start, 26):
        if learn[i] == False:
            learn[i] = True
            alphabet(i + 1, cnt + 1)
            learn[i] = False

# ---------------------------------------------
n, k = map(int, input().split())
words = [set(input()) for _ in range(n)]

if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    # 배운 단어 기록
    learn = [False] * 26
    # 공통 단어 배움 처리
    for x in ["a", "n", "t", "c", "i"]:
        learn[ord(x) - ord("a")] = True
    k -= 5

    # 배운 단어 제거 처리
    words_set = []
    for word in words:
        tmp = set()
        for w in word:
            if w not in ["a", "n", "t", "c", "i"]:
                tmp.add(w)
        words_set.append(tmp)

    ans = 0
    alphabet(0, 0)
    print(ans)
