from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n, m = map(int,input().split())
maps = [list(map(int,list(input()))) for _ in range(n)]

# 이동할 수 있는 빈칸 미리 구해놓기
group = [[-1] * m for _ in range(n)]
group_size = []

