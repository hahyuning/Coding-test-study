from collections import Counter
n = int(input())
for _ in range(n):
    s, t = input().split()
    if len(s) != len(t):
        print(s + " & " + t + " are NOT anagrams.")
    else:
        a = Counter(s)
        b = Counter(t)
        if a == b:
            print(s + " & " + t + " are anagrams.")
        else:
            print(s + " & " + t + " are NOT anagrams.")