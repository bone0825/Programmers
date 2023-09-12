def solution(n, s):
    answer = []
    mok = s//n
    r = s%n
    i = 0
    if mok == 0:
        return [-1]
    else:
        answer = [mok]*n
        while r > 0:
            answer[i] += 1
            i += 1
            r -= 1
    answer.sort()
    return answer