import sys

s = sys.stdin.readline().strip()
suffix_list = []

for i in range(len(s)):
    suffix_list.append(s[i:])

suffix_list.sort()

for x in suffix_list:
    print(x)
