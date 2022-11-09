# 2630 색종이 만들기 < 실버 2 >
from sys import stdin

result = {0:0, 1:0}

def solution(x, y, N, graph):
    std = graph[y][x]

    # 1 X 1 크기의 종이
    if N == 1:
        result[std] += 1
        return # 종료

    for ny in range(y, y+N):
        for nx in range(x, x+N):
            if std != graph[ny][nx]:
                # 4분할(Divide)
                solution(x, y, N//2, graph)
                solution(x+N//2, y, N//2, graph)
                solution(x, y+N//2, N//2, graph)
                solution(x+N//2, y+N//2, N//2, graph)
                return # 종료

    # N X N 크기의 종이
    result[std] += 1
    return # 종료

# input
N = int(stdin.readline())
graph = list(list(map(int,stdin.readline().split())) for _ in range(N))

# result
solution(0, 0, N, graph)
print(result[0])
print(result[1])