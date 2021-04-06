n = int(input())

list = [input() for _ in range(n)]
alphabet = [0 for _ in range(26)]

for x in list:
    i = 0
    while x:
        now = x[-1]
        alphabet[ord(now) - ord("A")] += pow(10, i)
        i += 1
        x = x[:-1]

alphabet.sort(reverse=True)
ans = 0
for i in range(9, 0, -1):
    ans += i * alphabet[9 - i]
print(ans)