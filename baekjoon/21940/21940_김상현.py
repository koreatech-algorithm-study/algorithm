# 21940 가운데에서 만나기 < 골드 4 >
from sys import stdin, maxsize

def solution(N,edges,K,C):
    answer = []

    # [0] 간선 초기화
    graph = [[maxsize] * (N+1) for _ in range(N+1)]
    for A, B, T in edges:
        graph[A][B] = T
    for i in range(1,N+1):
        graph[i][i] = 0

    # [2] 플로이드워셜 알고리즘
    for k in range(1,N+1):
        for j in range(1,N+1):
            for i in range(1,N+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j] # 최단 거리 갱신
    
    # [3] 최대 왕복시간 계산
    cities = [0] * (N+1)
    for X in range(1, N+1):
        maxValue = 0
        for c in C:
            if c == X or graph[c][X] == maxsize or graph[X][c] == maxsize: continue
            maxValue = max(maxValue, graph[X][c] + graph[c][X])
        cities[X] = maxValue
    
    # [4] 최소 왕복시간 계산
    target = min(cities[1:])
    for X in range(1,N+1):
        if cities[X] == target:
            answer.append(X)
    
    return answer

# input
N, M = map(int,stdin.readline().split())
edges = list(tuple(map(int,stdin.readline().split())) for _ in range(M))
K = int(stdin.readline())
C = list(map(int,stdin.readline().split()))

# result
result = solution(N,edges,K,C)
print(*result)