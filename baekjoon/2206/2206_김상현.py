# 2206 벽 부수고 이동하기 < 골드 3 >
from sys import stdin
from collections import deque

def solution(N,M,graph):

    visited = [[[0] * M for _ in range(N)] for _ in range(2)]
    visited[0][0][0] = 1
    queue = deque([(0, 0, 0)])

    # BFS 탐색
    while queue:
        x, y, z = queue.popleft()
        
        # 목적지 도달
        if x == M-1 and y == N-1: return visited[z][y][x]

        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = x + dx, y + dy

            # 한계 영역 설정
            if nx < 0 or nx >= M or ny < 0 or ny >= N: continue

            # 벽(1)에 다다른 경우
            if graph[ny][nx] == 1 and z == 0:
                queue.append((nx, ny, 1))
                visited[z+1][ny][nx] = visited[z][y][x] + 1

            # 벽이 아닌 경우(0)
            elif graph[ny][nx] == 0 and visited[z][ny][nx] == 0:
                queue.append((nx, ny, z))
                visited[z][ny][nx] = visited[z][y][x] + 1
    return -1

# input
N, M = map(int,stdin.readline().split())
graph = list( list(map(int,list(stdin.readline().strip()))) for _ in range(N))

# result
result = solution(N,M,graph)
print(result)