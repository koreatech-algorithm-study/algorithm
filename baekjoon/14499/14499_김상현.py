# 14499 주사위 굴리기 < 골드 4 >
from sys import stdin

def solution(N, M, x, y, graph, orders):

    move = [(0,0),(1,0),(-1,0),(0,-1),(0,1)]
    dice = [0,0,0,0,0,0]

    for order in orders:
        # [1] 명령에 따른 주사위 이동
        nx, ny = x + move[order][0], y + move[order][1]

        # [2] 경계값 확인 및 위치 갱신
        if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
        x, y = nx, ny 

        # [3] 주사위 굴리기
        if order == 1: # 동
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif order == 2: # 서
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif order == 3: # 북
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        elif order == 4: # 남
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        
        # [4] 이동한 칸의 값과 주사위의 바닥면 값 갱신
        if graph[y][x] == 0:
            graph[y][x] = dice[5]
        elif graph[y][x] != 0:
            dice[5], graph[y][x] = graph[y][x], 0
        
        print(dice[0])

# input
N, M, y, x, K = map(int,stdin.readline().split())
graph = [list(map(int,stdin.readline().split())) for _ in range(N)]
orders = list(map(int,stdin.readline().split()))

# result
solution(N, M, x, y, graph, orders)