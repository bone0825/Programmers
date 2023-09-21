def solution(n, words):
    temp = []
    for i in range(len(words)):
        cnt = 0
        if not temp:
            temp.append(words[i])
            continue
            
        for j in temp:
                if j == words[i]:
                    cnt =1
                    break
        if temp[-1][-1] != words[i][0]:
            cnt = 1
        else:
            temp.append(words[i])
        if cnt == 1:
            return [i%n+1 ,int(i/n)+1]
    return [0,0]
