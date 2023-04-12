def solution(s):
    s = list(map(int , s.split(' ')))
    max ,min = s[0], s[0]
    for i in s:
        if(max < i):
            max = i
        if(min > i):
            min = i
    
    answer = ('%d %d'%(min,max))
    return answer