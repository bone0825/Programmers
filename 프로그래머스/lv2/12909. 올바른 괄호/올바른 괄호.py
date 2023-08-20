def solution(s):
    temp = list(s)
    answer = 0
    for i in range(len(temp)):
        if answer < 0:
            return False
        if temp[i] == '(':
            answer += 1
        else:
            answer -= 1
    
    if answer == 0:
        return True
    else:
        return False