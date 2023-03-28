def solution(A,B):
    answer = 0
    tmp = []
    
    A.sort(reverse=True)
    B.sort()
    
    print(A)
    print(B)
    
    while A:
        a = A.pop()
        print(a)
        b = B.pop()
        print(b)
        answer += a*b
    return answer