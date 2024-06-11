import sys
sys.setrecursionlimit(10000000)

def solution(n, computers):
    visited = [False for _ in range(n)] # 방문 기록 확인
    check = 0 #연결된 횟수
    for i in range(n): #모든 컴퓨터에 대하여
        if visited[i] == False: #방문하지 않은 컴퓨터는
            check += 1
            answer(computers, visited, i)            
    return check

def answer(computer, visited, i):
    visited[i] = True #방문처리
    for j in range(len(computer)): #이전에 점검한 컴
        if visited[j] == False and computer[i][j] == 1:
            answer(computer, visited, j)