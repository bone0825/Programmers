def addEven(n):
    temp = 0
    for i in range(1,n+1):
        if i%2 == 1:
            temp = temp + i
    return temp
    
def addOdd(n):
    temp = 0
    for i in range(1,n+1):
        if i%2 == 0:
            temp = temp + i**2
    return temp
                
def solution(n):
    answer = 0
    if n%2 !=0 :
        return addEven(n)
    else:
        return addOdd(n)
    return answer