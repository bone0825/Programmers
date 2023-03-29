from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    sort_count = sorted(counter.items(), key = lambda item: item[1], reverse = True)
    
    for i in sort_count:
        if k <= 0:
            return answer
        k -= i[1]
        answer +=1
        """
    while(list(counter.values())[answer] < k):
        k= k - list(counter.values())[answer]
        answer += 1
    
    if(k != 0 and answer == 0):
        answer += 1
        """
    return answer
