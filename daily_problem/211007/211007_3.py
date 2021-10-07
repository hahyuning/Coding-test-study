import sys
input = sys.stdin.readline

n, m = map(int, input().split())
passwords = dict()

for _ in range(n):
    cite, password = input().rstrip().split()
    passwords[cite] = password

for _ in range(m):
    print(passwords[input().rstrip()])