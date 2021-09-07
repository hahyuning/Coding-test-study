from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    # 지도 확장
    a = ["*." + input().rstrip() + ".*" for _ in range(n)]
    n += 4
    m += 4
    a = ["*" * m, "*" + "." * (m - 2) + "*"] + a + ["*" + "." * (m - 2) + "*", "*" * m]

    # 열쇠 저장
    key = set(input().rstrip())
    door = [deque() for _ in range(26)]

    check = [[False] * m for _ in range(n)]
    q = deque()
    q.append((1, 1))
    check[1][1] = True
    ans = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            # 범위 검사 생략해도 됨
            if not check[nx][ny]:
                check[nx][ny] = True
                tmp = a[nx][ny]

                # 빈칸인 경우
                if tmp == ".":
                    q.append((nx, ny))
                # 문서인 경우
                elif tmp == "$":
                    ans += 1
                    q.append((nx, ny))
                # 문인 경우
                elif "A" <= tmp <= "Z":
                    # 열쇠가 있으면 큐에 삽입
                    if tmp.lower() in key:
                        q.append((nx, ny))
                    # 열쇠가 없으면 해당 문자 큐에 삽입
                    else:
                        door[ord(tmp) - ord("A")].append((nx, ny))
                # 열쇠인 경우
                elif "a" <= tmp <= "z":
                    q.append((nx, ny))
                    if tmp not in key:
                        key.add(tmp)
                        # 해당 열쇠로 열수 있는 문의 위치 큐에 삽입
                        q.extend(door[ord(tmp) - ord("a")])
    print(ans)