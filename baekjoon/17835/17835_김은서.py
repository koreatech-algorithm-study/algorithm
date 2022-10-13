"""
면접보는 승범이네(https://www.acmicpc.net/problem/17835)

풀이
- 면접장에서부터 시작하여 각 도시로 가는 거리를 갱신한다.
- heapq를 사용하여서 누적 거리가 짧은 노드부터 방문한다.
- 단, 한번 방문한 도시는 다시 방문하지 않는다. (heapq는 최소힙이므로 방문한 도시는 이미 최소 거리값이 결정된 상태이다.)
"""


from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline
INITIAL_STATE = -1


def solution(N, graph, destinations):
    queue = []
    for destination in destinations:  # 시작점은 면접장 위치
        heapq.heappush(queue, [0, destination])  # [현재 노드까지의 누적 거리, 현재 방문한 노드]

    distance = [INITIAL_STATE for _ in range(N + 1)]
    while queue:
        dist, curr = heapq.heappop(queue)
        if distance[curr] != INITIAL_STATE:  # 이미 도시를 방문함 → 값이 이미 (최솟값으로) 갱신된 상태임
            continue
        distance[curr] = dist

        neighbors = graph[curr]
        for next_dist, neighbor in neighbors:
            if distance[neighbor] == INITIAL_STATE:  # 아직 방문하지 않은 도시인 경우만 방문 가능
                heapq.heappush(queue, [dist + next_dist, neighbor])

    answer = max(distance)
    return [distance.index(answer), answer]


#
N, M, K = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    prev, next, w = map(int, input().split())
    graph[next].append([w, prev])  # 역방향으로 그래프를 연결 (나중에 면접장에서 탐색을 시작할 것이기 때문)
destinations = list(map(int, input().split()))  # destinations: 면접장
result = solution(N, graph, destinations)
for answer in result:
    print(answer)
