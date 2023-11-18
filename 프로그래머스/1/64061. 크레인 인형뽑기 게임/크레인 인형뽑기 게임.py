def checkDolls(basket):
    temp1 = basket.pop()
    temp2 = basket.pop()
    if temp1 == temp2:
        return 2
    else:
        basket.append(temp2)
        basket.append(temp1)
        return 0

def solution(board, moves):
    board.reverse()
    print(board)

    # Create new_board without zeros
    new_board = [[row[i] for row in board if row[i] != 0] for i in range(len(board[0]))]
    basket = []
    answer = 0

    for i in moves:
        if new_board[i-1]:
            doll = new_board[i-1].pop()
            basket.append(doll)
            if len(basket) > 1:
                answer += checkDolls(basket)


    return answer
