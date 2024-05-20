def solution(s):
    
    
    temp = s.lower().split(" ")
    for i in range(len(temp)):
        
        if(len(temp[i]) >= 1):
            temp[i] = temp[i][0].upper() + temp[i][1:]
        else:
            continue
            
    return ' '.join(temp)