def solution(s):
    answer = []
    temp = s.split(" ")
    for i in temp:
        answer.append(i.capitalize())
    
    return ' '.join(answer)