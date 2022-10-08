# 2447 별 찍기 - 10 < 골드 5 >
from sys import stdin

def solution(N):

    # '*' 로 구성된 N x N 크기의 배열 생성
    arr = [['*'] * N for _ in range(N)]

    # 재귀 함수
    def func(X, Y, N):

        # 현재 패턴의 크기가 3 x 3일 경우
        if N == 1:
            # 가운데 공백 패턴 생성
            arr[Y+1][X+1] = ' '
            return

        # 현재 패턴의 크기가 3 x 3 이상일 경우
        for y in range(3):
            for x in range(3):
                # 9등분된 배열 중 가운데 배열일 경우
                if x == 1 and y == 1:
                    # 가운데 공백 패턴 생성
                    for dy in range(Y + N, Y + 2 * N):
                        for dx in range(X + N, X + 2 * N):
                            arr[dy][dx] = ' '
                # 9등분된 배열 중 가운데 배열이 아닐 경우
                else:
                    # 인자를 변경하여 재귀함수 실행
                    func(X + x * N, Y + y * N, N // 3)
    
    # 재귀함수 실행
    func(0, 0, N//3)

    # 패턴 출력
    for a in arr:
        print(''.join(a))

N = int(stdin.readline())
solution(N)