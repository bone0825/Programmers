from collections import deque

def solution(operations):
    op = deque(operations)
    answer = []
    
    while op:
        data = op.popleft()
        if data[0] == 'I':
            answer.append(int(data[2:]))
        else:
            if data[2:] =='1':
                if answer:
                    answer.remove(max(answer))
            else:
                if answer:
                    answer.remove(min(answer))
                    
        print(answer)
                    
    if answer:
        return[max(answer),min(answer)]
    else:
        return [0,0]