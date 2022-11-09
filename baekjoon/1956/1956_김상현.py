# 1956 운동 <골드 4>
from sys import stdin
from heapq import heappop, heappush

def solution(graph, heap):

    while heap:
        c, b, a = heappop(heap) # currentLength, currentCountry, startingPoint

        # 출발지에 도착한 경우
        if b == a: return c

        # 현재 마을(b)과 연결된 다른 마을 heap에 추가 
        for nextCountry, length in graph[b]:
            heappush(heap, (c+length, nextCountry, a))
    
    # 운동 경로를 찾는 것이 불가능한 경우
    return -1

# input
V, E = map(int,stdin.readline().split())
graph = {i : [] for i in range(1,V+1)}
heap = []
for _ in range(E):
    a, b, c = map(int,stdin.readline().split())
    graph[a].append((b,c)) # 마을간의 경로를 저장
    heappush(heap, (c, b, a)) # 이동 경로 및 거리를 힙 자료구조에 저장

# result
result = solution(graph, heap)
print(result)