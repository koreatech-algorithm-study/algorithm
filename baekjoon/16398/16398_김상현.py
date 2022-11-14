# 16398 행성 연결 < 골드 4 >
from sys import stdin

def solution(N,edges):
    answer = 0
    parents = [i for i in range(N+1)]

    # [0] Union & Find
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        x = find(x)
        y = find(y)
        parents[max(x,y)] = min(x,y)
    
    # [1] Kruskal 알고리즘 적용
    for w, x, y in edges:
        x, y = find(x), find(y)
        if x == y: continue
        answer += w
        union(x,y)
    return answer

edges = []
N = int(stdin.readline())
for i in range(N):
    weight = list(map(int,stdin.readline().split()))
    for j in range(i+1,N):
        edges.append((weight[j],i,j))
edges.sort()

result = solution(N,edges)
print(result)