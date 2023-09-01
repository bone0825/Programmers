def solution(k, tangerine):
    arr = [0]* (max(tangerine)+1)
    temp1 = 0
    answer = 0
    
    while tangerine:
        temp = tangerine.pop()
        arr[temp] += 1
        
    arr.sort()
    while k > temp1:
        temp1 += arr.pop()
        answer += 1
        
    return answer