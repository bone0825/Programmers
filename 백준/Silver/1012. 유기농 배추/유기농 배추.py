import sys
sys.setrecursionlimit(10000000)

T = int(input())


def check(y, x):
    dx = [1,0,-1,0] #오른쪽 아래 왼쪽
    dy = [0,1,0,-1] # 오른쪽 아래 왼쪽

    farm[y][x] = 0 #지렁이 왔다 감~

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0 <= nx < M) and (0<= ny < N):
            if farm[ny][nx] == 1:
                check(ny,nx)

for _ in range(T):

    answer = 0
    M, N, K = map(int, input().split(" "))
    farm = [[0 for j in range(M)] for i in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split(" "))
        farm[Y][X] += 1

    for i in range(N):
        for j in range(M):
            if(farm[i][j] == 1):
                answer += 1
                check(i,j)
    print(answer)