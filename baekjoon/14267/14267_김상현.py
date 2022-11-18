# 14267 회사 문화 1 < 골드 4 >
from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

def solution(n,relations,compliments):
    # [0] 재귀 함수
    def recursive(i):
        points[i] += points[parents[i]]
        for child in children[i]:
            recursive(child)
    
    # [1] 칭찬 점수 초기화
    points = [0] * (n+1)
    for i, w in compliments:
        points[i] += w

    # [2] 양방향 트리 생성 및 초기화
    parents = {i : 0 for i in range(1,n+1)}
    children = {i : [] for i in range(1,n+1)}
    for i in range(1, n):
        parents[i+1] = relations[i]
        children[relations[i]].append(i+1)
        
    # [3] 재귀 함수 실행
    recursive(1)

    return points

# input
n, m = map(int,stdin.readline().split())
relations = list(map(int,stdin.readline().split()))
compliments = list(list(map(int,stdin.readline().split())) for _ in range(m))

# result
result = solution(n,relations,compliments)
print(*result[1:])