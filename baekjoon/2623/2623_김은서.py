"""
음악프로그램(https://www.acmicpc.net/problem/2623)
위상정렬
"""


from collections import defaultdict, deque


def solution(N, in_degree):
    # [1] 시작점을 queue에 답기
    queue = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:  # 시작점은 진입 차수가 0인 노드
            queue.append(i)

    # [2] BFS로 진입 차수가 0이 되는 노드들을 순차적으로 탐색
    answer = []
    while queue:
        curr = queue.popleft()
        answer.append(curr)

        for neighbor in graph[curr]:
            in_degree[neighbor] -= 1  # 진입 차수 1씩 감소
            if in_degree[neighbor] == 0:  # 이제 진입 차수가 0이 되는 노드는 방문 가능함
                queue.append(neighbor)

    # [3] 모든 노드를 다 탐색했다면 정답 / 아니라면 0 리턴
    if len(answer) == N:
        return answer[::-1]
    return [0]


#
N, M = map(int, input().split())
in_degree = [0 for _ in range(N + 1)]
graph = defaultdict(list)
for _ in range(M):
    singers = list(map(int, input().split()))
    for i in range(1, singers[0]):
        next, prev = singers[i], singers[i + 1]
        graph[prev].append(next)
        in_degree[next] += 1
result = solution(N, in_degree)
for num in result:
    print(num)
