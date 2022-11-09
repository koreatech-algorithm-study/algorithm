'''
baekjoon g2 면접보는 승범이네 
https://www.acmicpc.net/problem/17835
'''

import sys
import heapq

input = sys.stdin.readline
n, m, k = map(int, input().split())
INF = float('inf')
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))
interview_rooms = set(list(map(int, input().split())))


def dijkstra_heap(interview_rooms) :
    q = []
    distance = [INF] * (n+1)
    for interview_room in interview_rooms:
        heapq.heappush(q, (0, interview_room))  # 시작노드 정보 우선순위 큐에 삽입
        distance[interview_room] = 0
    
    while q:
        dist, node = heapq.heappop(q)
        # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우(=방문한 셈) 무시
        if distance[node] < dist:
            continue
        distance[node] = dist
        
        # 큐에서 뽑아낸 노드와 연결된 인접노드들 탐색
        for next, next_dist in graph[node]:
            cost = distance[node] + next_dist  # 시작->node거리 + node->node의인접노드 거리
            if cost < distance[next]:      # cost < 시작->node의인접노드 거리
                heapq.heappush(q, (cost, next))
    
    return distance.index(max(distance[1:])), max(distance[1:])


length_list = [INF] * (n+1)
distance = [INF] * (n+1)
ans_num, ans_length = dijkstra_heap(interview_rooms)
print(ans_num)
print(ans_length)
