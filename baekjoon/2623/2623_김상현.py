# 2623 음악프로그램 < 골드 3 >
from sys import stdin
from collections import deque

def solution(N, schedules):
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (N + 1)
    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
    graph = {i : [] for i in range(1,N + 1)}
    # 방향 그래프의 모든 간선 정보를 입력 받기
    for schedule in schedules:
        for i in range(1,schedule[0]):
            graph[schedule[i]].append(schedule[i+1])
            indegree[schedule[i+1]] += 1

    # 위상 정렬 함수
    def topology_sort():
        result = [] # 알고리즘 수행 결과를 담을 리스트
        queue = deque() # 큐 기능을 위한 deque 라이브러리 사용

        # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        for i in range(1, N + 1):
            if indegree[i] == 0:
                queue.append(i)

        # 큐가 빌 때까지 반복
        while queue:
            # 큐에서 원소 꺼내기
            now = queue.popleft()
            result.append(now)
            # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            for i in graph[now]:
                indegree[i] -= 1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[i] == 0:
                    queue.append(i)

        return result

    return topology_sort()

N, M = map(int,stdin.readline().split())
schedules = [list(map(int,stdin.readline().split())) for _ in range(M)]
result = solution(N, schedules)

if len(result) != N: # 현재 그래프가 사이클이 존재한다면
    print(0)
else:
    for r in result:print(r)