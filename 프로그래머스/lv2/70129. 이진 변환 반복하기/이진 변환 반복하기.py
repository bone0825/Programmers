def solution(s):
    answer = []
    repeat = 0
    removed = 0
    temp = list(s)

    while len(temp) > 1:
        repeat += 1
        new_temp = [values for values in temp if values != '0']
        removed += (len(temp) - len(new_temp))
        temp = list(format(len(new_temp), 'b'))
        
    answer.append(repeat)
    answer.append(removed)
    return answer