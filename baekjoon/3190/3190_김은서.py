"""
뱀(https://www.acmicpc.net/problem/3190)
"""

from collections import deque


def in_range(row, col, N):
    if 0 <= row < N and 0 <= col < N:
        return True
    return False


def solution(N, apple, seconds, directions):
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 우 하 좌 상
    curr_move_index = 0
    snake = deque([[0, 0]])  # 뱀의 이동 경로 저장 / snake_path[0]는 꼬리임
    total_seconds = 0

    while True:
        # [1] 만약 n초가 지난 경우 방향 바꾸기
        if len(seconds) > 0 and total_seconds == seconds[0]:
            seconds.popleft()
            direction = directions.popleft()
            if direction == "D":
                curr_move_index = (curr_move_index + 1) % 4  # 시계
            else:
                curr_move_index = (curr_move_index + 3) % 4  # 반시계

        # [2-1] 머리를 다음 칸으로 이동한다.
        mrow, mcol = moves[curr_move_index]
        next_row = snake[0][0] + mrow
        next_col = snake[0][1] + mcol

        # [2-2] 만약 범위를 벗어나거나 + 자기자신과 닿을 경우 종료
        if not in_range(next_row, next_col, N) or [next_row, next_col] in snake:
            return total_seconds + 1

        # [2-3] 사과 유무 체크
        if apple[next_row][next_col]:
            apple[next_row][next_col] = False
            snake.appendleft([next_row, next_col])  # 머리 이동
        else:
            snake.appendleft([next_row, next_col])  # 머리 이동
            snake.pop()  # 꼬리 자르기

        total_seconds += 1


# 입력 및 실행
N = int(input())
apple = [[False for _ in range(N)] for _ in range(N)]

K = int(input())
for _ in range(K):
    row, col = map(int, input().split())
    apple[row - 1][col - 1] = True

L = int(input())
seconds = deque()
directions = deque()
for _ in range(L):
    second, direction = input().split()
    seconds.append(int(second))
    directions.append(direction)

result = solution(N, apple, seconds, directions)
print(result)
