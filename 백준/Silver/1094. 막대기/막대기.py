# 64 32 16 8 4 2 1
X = int(input())
size = [1,2,4,8,16,32,64]
answer = 0

while(X != 0 and size):
    if(X < size[-1]):
        size.pop()
    else:
        X -= size.pop()
        answer += 1

print(answer)
