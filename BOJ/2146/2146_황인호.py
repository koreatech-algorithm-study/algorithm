'''
https://www.acmicpc.net/problem/2146
'''

from collections import deque
import numpy as np
n = int(input())
m = []
start = ()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    m.append(list(map(int, input().split(' '))))
    if 1 in m[i] and len(start) == 0: start = (i, m[i].index(1))

visited = [[False]*n for _ in range(n)]
q = deque([start])
visited[start[0]][start[1]] = True
island = []
tmp = []

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            # 바다를 만나면 해안가라 판단하여 좌표추가
            if m[nx][ny] == 0 and not (x, y) in tmp: tmp.append((x, y))
            if not visited[nx][ny] and m[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True

    # q에 좌표가 없다면 해당 섬을 다 방문한 것이라 판단, 다음 섬의 좌표 append
    if not q:
        island.append(tmp)
        tmp = []
        for i in range(n):
            for j in range(n):
                if m[i][j] == 1 and not visited[i][j] and not q:
                    q.append((i, j))
                    visited[i][j] = True

dist = []
# 각 섬의 해안가 간의 거리 계산
for i in range(len(island)):
    for j in range(i+1, len(island)):
        [[dist.append(abs(k[0] - t[0]) + abs(k[1] - t[1]) - 1) for k in island[j]] for t in island[i]]
        if 1 in dist: break

d = min(dist)
while d < 1:
    dist.remove(d)
    d = min(dist)
print(d)