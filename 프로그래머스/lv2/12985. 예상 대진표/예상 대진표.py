def solution(n,a,b):
    answer = 1
    
    while True:
        if((b-a == 1) and (b%2 == 0))or ((a-b == 1)and (a%2 == 0)):
            break
        answer += 1
        if a %2 == 0:
            a = a/2
        else:
            a = (a+1)/2
            
        if b % 2 == 0:
            b = b/2
        else:
            b = (b+1)/2
            
        a = int(a)
        b = int(b)
    
    return answer