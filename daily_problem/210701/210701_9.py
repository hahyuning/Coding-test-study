from collections import defaultdict
import sys
input = sys.stdin.readline

tree = defaultdict(int)
cnt = 0
while True:
    x = input().rstrip()
    if not x:
        break
    cnt += 1
    tree[x] += 1

key = list(tree.keys())
key.sort()
for x in key:
    print("%s %.4f" %(x, tree[x] / cnt * 100))