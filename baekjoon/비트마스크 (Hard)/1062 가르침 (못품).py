def teach(index, k, mask):
    # 불가능한 경우
    if k < 0:
        return 0
    if index == 26:
        return count(mask, words)

    ans = 0
    ans = max(ans, teach(index + 1, k - 1, mask | (1 << index)))
    if index not in [ord('a') - ord('a'), ord('n') - ord('a'), ord('t') - ord('a'), ord('i') - ord('a'),
                     ord('c') - ord('a')]:
        ans = max(ans, teach(index + 1, k, mask))

    return ans

def count(mask, words):
    cnt = 0
    for word in words:
        # 배우지 않은 알파벳이 있는지 확인
        if (word & ((1 << 26) - 1 - mask)) == 0:
            cnt += 1
    return cnt

n, k = map(int, input().split())
words = [0] * n
for i in range(n):
    word = input()
    for w in word:
        # 각각의 word를 비트마스크로 바꿔서 추가
        words[i] |= (1 << (ord(w) - ord('a')))

print(teach(0, k, 0))