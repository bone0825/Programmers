def solution(n):
    cnt = 1
    status = 0
    x, y = 0, 0
    answer = [[0 for j in range(n)] for i in range(n)] # 배열 초기화
    while cnt <= n ** 2:
        if status == 0:  # +x

            answer[y][x] = cnt

            if x + 1 == n or answer[y][x + 1] != 0:
                if cnt == n**2:
                    break
                status = 1
                continue


            x += 1

        elif status == 1:  # +y

            answer[y][x] = cnt

            if  y + 1 == n or answer[y + 1][x] != 0:
                if cnt == n**2:
                    break
                status = 2
                continue

            y += 1


        elif status == 2:  # -x

            answer[y][x] = cnt

            if answer[y][x - 1] != 0:
                if cnt == n**2:
                    break
                status = 3
                continue

            x -= 1

        elif status == 3:  # -y

            answer[y][x] = cnt
            if answer[y - 1][x] != 0:
                if cnt == n**2:
                    break
                status = 0
                continue


            y -= 1

        cnt += 1
    return answer