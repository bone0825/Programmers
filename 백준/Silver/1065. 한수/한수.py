T = input()

if (len(T) < 3):
    print(int(T))

else:
    check = 99
    T = int(T)

    for i in range(100,T + 1):
        i = str(i)
        if ((int(i[0]) + int(i[2]))/ 2 == int(i[1])):
            check += 1
    print(check)
