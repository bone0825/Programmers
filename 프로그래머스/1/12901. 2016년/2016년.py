def solution(a, b):
    day = [31,29,31,30,31,30,31,31,30,31,30,31]
    DoW = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    total_day = 0
    for i in range(a - 1):
        total_day += day[i]
    total_day += b - 1
    return DoW[total_day%7]