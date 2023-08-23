def solution(n):
#     repeat = 0
#     a = int(n/2)+1 if n % 2 != 0 else n/2
#     k = a/2
#     while True:
#         sum = 0
#         for i in range(a,0,-1):
#             sum += i
#             if sum == n:
#                 repeat += 1
#             if sum >= n:
#                 break
#         a -= 1
#         if a < 0:
#             break
        
#     return repeat + 1
    answer = 0
    for i in range(1,n+1):
        sum = 0
        for j in range(i,n+1):
            sum += j
            if sum == n:
                answer += 1
                break
            elif sum >n:
                break
    return answer