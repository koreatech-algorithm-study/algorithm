'''
baekjoon g4 빙산
https://www.acmicpc.net/problem/2573
'''
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
matrix = []
visit = [[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    matrix.append(list(map(int, input().split())))

def bfs(x, y):
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    q = deque()
    melt_q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] != 0 and visit[nx][ny] == False:
                    visit[nx][ny] = True
                    q.append([nx, ny])
                elif matrix[nx][ny] == 0:
                    matrix[x][y] -= 1
        if matrix[x][y] <= 0:
            matrix[x][y] = -1
            melt_q.append([x, y])
    while melt_q:
        x, y = melt_q.popleft()
        matrix[x][y] = 0
    
ans = 0
while True:
    visit = [[False for _ in range(M)] for _ in range(N)]
    iceburg = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if visit[i][j] == True:
                continue
            if matrix[i][j] > 0:
                # 빙산 발견시 빙산 탐색 및 녹이기
                visit[i][j] = True
                all_icebergs_melt = False
                iceburg += 1
                bfs(i, j)
    # 빙산이 두개 이상이라면 결과 출력 및 종료
    # 빙산이 없다면 0 출력 및 종료
    if iceburg == 0:
        print(0)
        break
    elif iceburg > 1:
        print(ans)
        break
    
    ans += 1