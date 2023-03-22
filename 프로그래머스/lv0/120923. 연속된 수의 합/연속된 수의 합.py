def solution(num, total):
    answer = []
    cnt = -100;
    while(True):
        for i in range(num):
            answer.append(cnt + i)
            
        if(sum(answer) == total):
            break
        else:
            answer = []
            cnt = cnt + 1
    
    return answer
        