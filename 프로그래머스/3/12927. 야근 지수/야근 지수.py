import heapq
def solution(n, works):
    answer = 0
    heap = []
    
    if (sum(works) < n):
        return 0
    
    for i in works:
        heapq.heappush(heap,-i)
    
    while (n>0):
        heapq.heappush(heap,heapq.heappop(heap)+ 1)
        n -= 1
    
    while(heap):
        answer += heapq.heappop(heap)**2
    
    
    
    return answer