import sys
input = sys.stdin.readline

alphabet = [0] * 26
n = int(input())
for _ in range(n):
    s = input().rstrip()
    alphabet[ord(s[0]) - ord("a")] += 1

ans = ""
for i, x in enumerate(alphabet):
    if x >= 5:
        ans += chr(i + ord("a"))

if len(ans) == 0:
    print("PREDAJA")
else:
    print(ans)