# 17835 면접보는 승범이네 < 골드 2 >
from sys import maxsize, stdin, maxsize
from collections import defaultdict, deque

def solution(N, graph, starts):

    city, dist = 0, 0

    distance = [maxsize] * (N+1) # 면접장 기준에서의 최단 거리 정보를 담은 리스트
    queue = deque(starts) # 면접장 위치 정보

    # 면접장 거리값 0으로 초기화
    for start in starts:
        distance[start] = 0

    # 면접장 기준 각 도시 별 최단 거리 구하기
    while queue:    
        currentNode = queue.popleft()
        # 현재 도시와 연결된 모든 도시와 도시 간의 거리 탐색
        for nextNode, weight in graph[currentNode]: 
            # 최소 거리값 갱신
            if distance[nextNode] > distance[currentNode] + weight:
                distance[nextNode] = distance[currentNode] + weight
                queue.append(nextNode)
    
    # 최장거리 도시 위치 탐색
    for i in range(1,N+1):
        if distance[i] != maxsize and distance[i] > dist:
            city, dist = i, distance[i]
    
    return city, dist
    
# 입력
graph = defaultdict(list)
N, M, K = map(int,stdin.readline().split())
for _ in range(M):
    U, V, C = map(int,stdin.readline().split())
    graph[V].append((U,C)) # 주어진 방향의 역뱡향으로 그래프 생성
starts = list(map(int,stdin.readline().split()))

# solution()
city, dist = solution(N, graph, starts)

# 결과
print(city)
print(dist)