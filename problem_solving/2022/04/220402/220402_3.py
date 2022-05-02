def solution(dist):
    ans = []

    def dfs(now, points):
        if now == len(dist):
            tmp = sorted(points.items(), key=lambda x:x[1])
            res = []
            for x, y in tmp:
                res.append(x)
            ans.append(res)
            return

        if not points:
            points[now] = 0
            dfs(now + 1, points)
            del points[now]
        else:
            for d in [-dist[now][0], dist[now][0]]:
                check = False
                for nxt in points.keys():
                    dd = abs(d - points[nxt])
                    if dist[now][nxt] != dd:
                        check = True

                if not check:
                    points[now] = d
                    dfs(now + 1, points)
                    del points[now]

    dfs(0, dict())
    ans.sort()
    return ans

solution([[0,2,3,1],[2,0,1,1],[3,1,0,2],[1,1,2,0]])