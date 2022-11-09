# 7569 토마토 < 골드 5>
from sys import stdin
from itertools import chain

def solution(M, N, H, box):
    # 토마토들이 모두 익는 최소 일수
    answer = 0 

    # 익지 않은 토마토의 개수
    rawTomatoes = list(chain(*list(chain(*box)))).count(0) 

    # 익은 토마토가 존재하는 지점
    startPoints = set() 
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x] == 1:
                    startPoints.add((x,y,z))

    while True:
        # 익게될 토마토가 존재하는 지점
        newPoints = set() 
        
        # 익은 토마토가 존재하는 지점(startPoint)를 기준으로 여섯 방향 탐색
        for x, y, z in startPoints:
            for dx, dy, dz in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
                nx, ny, nz = x + dx, y + dy, z + dz
                if nx < 0 or nx >= M or ny < 0 or ny >= N or nz < 0 or nz >= H or box[nz][ny][nx] != 0: continue
                newPoints.add((nx,ny,nz))
        
        # 익게될 토마토가 존재하지 않는다면
        if not newPoints:
            break

        # 토마토 익는중...
        for x, y, z in newPoints:
            box[z][y][x] = 1
            rawTomatoes -= 1

        # 익은 토마토가 존재하는 지점(startPoint)을 익게될 토마토가 존재하는 지점(newPoints)로 갱신
        startPoints = newPoints

        # 토마토들이 모두 익는 최소 일수 1 증가
        answer += 1

    # 만약 모든 토마토가 익지 않았다면
    if rawTomatoes != 0:
        return - 1
    # 모든 토마토가 익었다면
    else:
        return answer

# input
M, N, H = map(int,stdin.readline().split()) # 가로, 세로, 높이
box = [ list(list(map(int,stdin.readline().split())) for _ in range(N)) for _ in range(H) ]

result = solution(M, N, H, box)
print(result)