# 1719 택배 < 골드 3 >
from sys import stdin, maxsize
from collections import defaultdict
from heapq import heappop, heappush

# 다잌스트라 풀이
def solution1(n,edges):

    # [0] 경로표, 가장 먼저 거쳐야 하는 집하장 표 생성
    graph = [[maxsize] * (n+1) for _ in range(n+1)]
    answer = [["-"] * (n+1) for _ in range(n+1)]

    for i in range(1,n+1):
        graph[i][i] = 0 # i → i 이동 차단

        # [1] 초기 이동 경로 heap 생성
        heap = []
        for node, weight in edges[i]:
            heappush(heap, (weight, node, node)) # (가중치, 현재 정점, 가장 먼저 거쳐야 하는 정점)
        
        # [2] 다잌스트라 알고리즘 적용
        while heap:
            w, node, wayPoint = heappop(heap)
            if graph[i][node] > w:
                graph[i][node] = w
                answer[i][node] = wayPoint
                for nextNode, weight in edges[node]:
                    heappush(heap, (w+weight, nextNode, wayPoint))

    # [3] 결과 출력
    for y in range(1,n+1):
        for x in range(1,n+1):
            print(answer[y][x], end=' ')
        print()

# 플로이드워셜 풀이
def solution2(n,edges):
    # [0] 경로표, 가장 먼저 거쳐야 하는 집하장 표 생성
    graph = [[maxsize] * (n+1) for _ in range(n+1)]
    answer = [["-"] * (n+1) for _ in range(n+1)]

    # [1] 경로표, 가장 먼저 거쳐야 하는 집하장 표 초기화
    for n1, n2, w in edges:
        graph[n1][n2] = w
        graph[n2][n1] = w
        answer[n1][n2] = n2
        answer[n2][n1] = n1
    for i in range(1,n+1):
        graph[i][i] = 0
    
    # [2] 플로이드워셜 알고리즘 적용
    for k in range(1,n+1):
        for j in range(1,n+1):
            for i in range(1,n+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j] # 최단 거리 갱신
                    answer[i][j] = answer[i][k] # 가장 먼저 거쳐야 하는 집하장 갱신
    
    # [3] 결과 출력
    for y in range(1,n+1):
        for x in range(1,n+1):
            print(answer[y][x], end=' ')
        print()


    
# input
n, m = map(int,stdin.readline().split())
edges1 = defaultdict(list)
edges2 = []
for _ in range(m):
    n1, n2, w = map(int,stdin.readline().split())
    edges1[n1].append((n2,w))
    edges1[n2].append((n1,w))
    edges2.append((n1,n2,w))

# result
solution1(n,edges1)
solution2(n,edges2)