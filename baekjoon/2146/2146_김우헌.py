'''
baekjoon g3 다리만들기
https://www.acmicpc.net/problem/2146
'''

from collections import deque, defaultdict
from itertools import combinations, product
import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

visit =[[False for _ in range(N)] for _ in range(N)]
country = defaultdict(set)
country_num = 1
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

# 국가 구분
for r in range(N):
    for c in range(N):
        if visit[r][c] == False and matrix[r][c] == 1:
            q = deque()
            q.append((r, c))
            visit[r][c] = True
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == False:
                        if matrix[nx][ny] == 1:
                            visit[nx][ny] = True
                            q.append((nx, ny))
                        elif matrix[nx][ny] == 0:
                            country[country_num].add((x, y))
            country_num += 1

min_answer = float('inf')
country_mapping_set = combinations(country.values(), 2)

for c1, c2 in country_mapping_set:
    for p1 in c1:
        for p2 in c2:
            min_answer = min(min_answer, abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) - 1)
# for c1, c2 in country_mapping_set:
#     bridge_mapping_set = product(c1, c2)
#     curr = min([abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) - 1 for p1, p2 in bridge_mapping_set])
#     min_answer = min(min_answer, curr)
print(min_answer)
