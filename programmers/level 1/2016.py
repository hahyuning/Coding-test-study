def solution(a, b):
    day_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    last_date = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 1월 1일은 금요일

    start_day = 5

    start_day += sum(last_date[: a])
    start_day += (b - 1)
    start_day %= 7
    return day_list[start_day]

print(solution(1, 3))