"""
다리 만들기(https://www.acmicpc.net/problem/2146)
풀이방법: DFS
"""

import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 6)


ISLAND = 1


def solution(N, arr):
    def in_range(row, col):
        if 0 <= row < N and 0 <= col < N:
            return True
        return False

    def dfs(row, col, visited):
        if visited[row][col]:
            return
        visited[row][col] = True

        edges = []  # 바다와 맞닿아있는 가장자리 영역
        for mr, mc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr = row + mr
            nc = col + mc
            if not in_range(nr, nc) or visited[nr][nc]:
                continue

            if arr[nr][nc] == ISLAND:
                edges += dfs(nr, nc, visited)
            else:  # 현재 섬은 바다와 맞닿아있는 가장자리 영역
                if [row, col] not in edges:
                    edges.append([row, col])

        return edges

    # 1) DFS로 섬 탐색 + 각 섬의 가장자리 영역을 edges에 추가하기
    visited = [[False for _ in range(N)] for _ in range(N)]
    edges = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == ISLAND and not visited[r][c]:
                edges.append(dfs(r, c, visited))

    # 2) 두 섬의 가장자리 영역 사이의 거리 중 최단거리 구하기
    all_combination_cases = combinations(edges, 2)
    min_distance = float("inf")
    for i1, i2 in all_combination_cases:
        for i1_row, i1_col in i1:
            for i2_row, i2_col in i2:
                cur_distance = abs(i1_row - i2_row) + abs(i1_col - i2_col) - 1
                min_distance = min(min_distance, cur_distance)

    return min_distance


# 입력 및 실행
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
result = solution(N, arr)
print(result)