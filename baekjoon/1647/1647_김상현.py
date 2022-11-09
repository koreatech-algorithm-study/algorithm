# 1647 도시 분할 계획 < 골드 4 >
from sys import stdin

def solution(N,edges):
    answer = 0
    graph = list(range(N+1))

    # UNION
    def union(x, y):
        x = find(x)
        y = find(y)
        graph[max(x,y)] = min(x,y)

    # FIND
    def find(x):
        if x != graph[x]:
            graph[x] = find(graph[x])
        return graph[x]

    # KRUSKAL MINIMUM SPANNING TREE
    for A, B, C in edges:
        if N == 2: break # 마을이 두개로 분리된 상태
        if find(A) != find(B): # 사이클 형성하는 간선 무시
            answer += C
            union(A,B)
            N -= 1

    return answer

# input
N, M = map(int,stdin.readline().split())
edges = []
for _ in range(M):
    A, B, C = map(int,stdin.readline().split())
    edges.append((A,B,C))
edges.sort(key=lambda x : x[2]) # 가중치(C)를 기준으로 정렬

#result
result = solution(N,edges)
print(result)