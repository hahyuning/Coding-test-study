import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    all = input().rstrip().split()
    others = []
    while True:
        s = input().rstrip()
        if s == "what does the fox say?":
            ans = []
            for x in all:
                if x not in others:
                    ans.append(x)
            print(" ".join(ans))
            break

        tmp = s.split()
        others.append(tmp[-1])


