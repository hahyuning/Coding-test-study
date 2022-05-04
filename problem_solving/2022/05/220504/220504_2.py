from collections import defaultdict

def file_count(now):
    cnt = 0
    for nxt, type in graph[now]:
        if type == 0:
            cnt += 1
        else:
            cnt += file_count(nxt)

    file[now] = cnt
    return cnt

def file_kind_count(now):
    file_set = set()
    for nxt, type in graph[now]:
        if type == 0:
            file_set.add(nxt)
        else:
            tmp = file_kind_count(nxt)
            for x in tmp:
                file_set.add(x)

    file_kind[now] = len(file_set)
    return file_set


if __name__ == '__main__':
    n, m = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(n + m):
        p, f, c = input().rstrip().split()
        # 폴더일 경우 c=1, 파일일 경우 c=0
        graph[p].append((f, int(c)))

    file = defaultdict(int)
    file_kind = defaultdict(int)
    file_count("main")
    file_kind_count("main")

    q = int(input())
    for _ in range(q):
        s = input().rstrip().split("/")[-1]
        print(file_kind[s], file[s])

