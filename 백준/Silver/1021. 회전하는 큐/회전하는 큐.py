from collections import deque

M,N = map(int,input().split())
target = list(map(int, input().split()))
target.reverse()

temp = deque()
answer = 0

for i in range(1, M+1):
    temp.append(i)

while(target):
    if target[-1] == temp[0]:
        target.pop()
        temp.popleft()
    else:
        temp_front = temp.copy()
        temp_back = temp.copy()
        while(True):
            answer += 1
            temp_front.rotate()
            temp_back.rotate(-1)
            if(temp_front[0] == target[-1]):
                target.pop()
                temp_front.popleft()
                temp = temp_front
                break
            elif(temp_back[0] == target[-1]):
                target.pop()
                temp_back.popleft()
                temp = temp_back
                break

print(answer)