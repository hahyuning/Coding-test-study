from itertools import permutations

def solution(idx, s):
    if len(s) == k:
        for x in p:
            tmp = ""
            for i in x:
                tmp += str(s[i])
            ans.add(tmp)
        return

    if idx >= n:
        return

    solution(idx + 1, s + [a[idx]])
    solution(idx + 1, s)


n = int(input())
k = int(input())
p = list(permutations([i for i in range(k)]))
a = [int(input()) for _ in range(n)]
ans = set()
solution(0, [])
print(len(ans))