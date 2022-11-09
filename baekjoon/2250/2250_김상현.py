# 2550 트리의 높이와 너비 < 골드 2 >
from sys import stdin
from collections import defaultdict

count = 1

def solution(N,edges):

    LAYER, WIDTH = 0, 0
    layerList = defaultdict(list)
    nodes = [[None,None] for _ in range(N+1)]
    rootCandidate = [0] * (N+1)

    # [0] 중위 순회 함수
    def inOrder(num, layer):
        global count
        left, right = nodes[num]
        if left != -1: inOrder(left, layer+1)
        layerList[layer].append(count)
        count += 1
        if right != -1: inOrder(right, layer+1)

    # [1] 이진트리 만들기
    for value, left, right in edges:
        nodes[value][0] = left
        nodes[value][1] = right

        if left != -1: rootCandidate[left] += 1
        if right != -1: rootCandidate[right] += 1

    # [2] root 노드 찾기
    for i in range(1,N+1):
        if rootCandidate[i] == 0:
            root = i

    # [3] 중위 순회
    inOrder(root,1)

    # [4] 너비가 가장 넓은 레벨과 그 레벨의 너비 탐색
    for key in sorted(layerList):
        values = layerList[key]
        width = max(values) - min(values) + 1
        if WIDTH < width:
            LAYER, WIDTH = key, width

    return LAYER, WIDTH

N = int(stdin.readline())
edges = [list(map(int,stdin.readline().split())) for _ in range(N)]

layer, width = solution(N,edges)
print(layer, width)