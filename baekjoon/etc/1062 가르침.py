import sys
input = sys.stdin.readline

def dfs(j, cnt):
    global answer
    if cnt == k:
        read = 0
        for word in compressed_list:
            for w in word:
                if not learn[ord(w) - ord("a")]:
                    break
            else:
                read += 1
        answer = max(answer, read)
        return

    for i in range(j, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False


n, k = map(int, input().split())
word_list = [input().rstrip() for _ in range(n)]

if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    k -= 5
    compressed_list = []
    answer = 0

    learn = [False] * 26
    for x in ["a", "n", "t", "i", "c"]:
        learn[ord(x) - ord("a")] = True

    for word in word_list:
        temp_set = set()
        for a in word:
            if a not in ["a", "n", "t", "i", "c"]:
                temp_set.add(a)
        compressed_list.append(temp_set)

    dfs(0, 0)
    print(answer)




