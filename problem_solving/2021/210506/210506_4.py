from collections import Counter

# A, C, G, T
n, m = map(int, input().split())
a = [input() for _ in range(n)]
dna = ""
h = 0

for j in range(m):
    cnt = {"A": 0, "C":0, "G":0, "T":0}
    for i in range(n):
        cnt[a[i][j]] += 1

    cnt = Counter(cnt)
    max_letter = cnt.most_common(1)
    dna += max_letter[0][0]
    h += (n - max_letter[0][1])

print(dna)
print(h)

