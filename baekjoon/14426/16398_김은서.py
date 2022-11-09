"""
행성 연결(https://www.acmicpc.net/problem/16398)
"""

import heapq


def solution(N, graph):
    queue = [[0, 0]]  # weight, curr_node
    visited = [False for _ in range(N)]
    total_weight = 0
    while queue:
        weight, curr_node = heapq.heappop(queue)
        if visited[curr_node]:
            continue
        visited[curr_node] = True
        total_weight += weight
        for next_node in range(N):
            if curr_node != next_node and not visited[next_node]:
                heapq.heappush(queue, [graph[curr_node][next_node], next_node])
    return total_weight


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
result = solution(N, graph)
print(result)
