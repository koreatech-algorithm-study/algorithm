# 2146 다리 만들기 < 골드 3>
from sys import stdin
from collections import deque, defaultdict

move = [(1,0),(-1,0),(0,1),(0,-1)] # 상하좌우

def solution(N,lst):
    answer = 10001 # 최단 경로
    graph = [[0] * N for _ in range(N)] # 섬 분할 graph
    startPoints = defaultdict(list) # 각 섬의 육지 좌표를 저장하는 딕셔너리

    # 섬 분할하기, dfs 활용
    count = 0
    for y in range(N):
        for x in range(N):
            if lst[y][x] == 1:
                count += 1
                stack = [(x, y)]
                while stack:
                    x, y = stack.pop()
                    graph[y][x] = count
                    lst[y][x] = 0
                    for dx, dy in move:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or nx >= N or ny < 0 or ny >= N or lst[ny][nx] != 1: continue
                        stack.append((nx,ny))

    # 각 섬의 육지 좌표 추출      
    for y in range(N):
        for x in range(N):
            if graph[y][x] != 0:
                startPoints[graph[y][x]].append((x,y))

    # 최단 경로를 찾는 BFS
    for key, values in startPoints.items(): # key : 섬 이름, values : 섬의 육지 좌표
        
        visited = [[-1] * N for _ in range(N)]

        for x, y in values: visited[y][x] = 0 # 현재 섬의 육지 좌표 0으로 초기화

        queue = deque(values) # 섬의 육지 좌표
        check = False
        while queue:
            x, y = queue.popleft()
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                # graph 범위를 넘어가는 경우
                if nx < 0 or nx >= N or ny < 0 or ny >= N: continue 

                # 현재 섬에서 다른 섬에 연결된 경우
                if graph[ny][nx] > 0 and graph[ny][nx] != key:
                    answer = min(answer, visited[y][x])
                    # 현재 섬에 대한 조사 종료
                    check = True
                    break 

                # 현재 섬에서 처음 접근한 바다(0)를 만난 경우
                if graph[ny][nx] == 0 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x]+1
                    queue.append((nx, ny))
                
                # 현재 섬에 대한 조사 종료
                if check: break
        for v in visited:
            print(v)
        print()
    return answer

N = int(stdin.readline())
lst = [list(map(int,stdin.readline().split())) for _ in range(N)]

print(solution(N,lst))