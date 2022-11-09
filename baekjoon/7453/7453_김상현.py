# 7453 합이 0인 네 정수 < 골드 2 >
from sys import stdin

def solution(N, arr):
    answer = 0

    # [1] 4개의 리스트 2개로 병합
    AB, CD = [], []
    for i in range(N):
        for j in range(N):
            AB.append(arr[i][0] + arr[j][1])
            CD.append(arr[i][2] + arr[j][3])
    AB.sort()
    CD.sort(reverse = True)

    p1, p2 = 0, 0
    length = N*N

    # [2] 투포인터 체크
    while p1 < length and p2 < length:
        v1, v2 = AB[p1], CD[p2]
        if v1 + v2 == 0:
            n1, n2 = 0, 0
            while v1 == AB[p1] and p1 < length:
                p1, n1 = p1+1, n1+1
                if p1 == length: break
            while v2 == CD[p2] and p2 < length:
                p2, n2 = p2+1, n2+1
                if p2 == length: break
            answer += n1 * n2
        elif v1 + v2 > 0:
            p2 += 1
        elif v1 + v2 < 0:
            p1 += 1
    return answer

# input
N = int(stdin.readline())
arr = list(list(map(int,stdin.readline().split())) for _ in range(N))

# result
result = solution(N, arr)
print(result)