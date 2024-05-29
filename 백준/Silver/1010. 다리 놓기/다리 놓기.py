temp = int(input())
answer = []

for _ in range(temp):
    sum = 1
    n, m = map(int, input().split(" "))
    if (n == 1):
        answer.append(m)
    elif (n == m):
        answer.append(sum)
    else:
        for i in range(m, m - n, -1):
            sum *= i
        for i in range(1,n + 1):
            sum = sum//i

        answer.append(int(sum))

for i in answer:
    print(i)




