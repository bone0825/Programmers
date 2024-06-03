T = input()

if (len(T) < 3):
    print(int(T))

else:
    check = 99
    T = int(T)

    for i in range(100, T + 1):
        temp = []
        while (i):
            temp.append(i % 10)
            i = i // 10
        if ((temp[-1] - temp[-2]) == (temp[-2] - temp[-3])):
            check += 1
    print(check)

