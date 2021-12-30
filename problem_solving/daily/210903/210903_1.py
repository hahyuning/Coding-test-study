n = int(input())
grade = []
for _ in range(n):
    a, b = map(int, input().split())
    grade.append((a, b))

d = [[0] * 6 for _ in range(n + 1)]
max_val = 0
max_grade = 0

for i in range(1, n + 1):
    a = grade[i - 1][0]
    b = grade[i - 1][1]

    if a > b:
        a, b = b, a

    d[i][a] = d[i - 1][a] + 1
    if d[i][a] > max_val:
        max_val = d[i][a]
        max_grade = a

    if a != b:
        d[i][b] = d[i - 1][b] + 1
        if d[i][b] > max_val:
            max_val = d[i][b]
            max_grade = b

print(max_val, max_grade)