'''
baekjoon g4 뱀
https://www.acmicpc.net/problem/3190
'''
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())
snake = deque()
apple = set()
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
snake.append((0, 0))
for _ in range(K):
    r, c = map(int, input().split())
    apple.add((c-1, r-1))
L = int(input())
command = deque()
for _ in range(L):
    x, c = input().split()
    command.append((int(x), c))

t = 1
d = 0
while True:
    # 부딛히지 않는다면 머리 이동
    x, y = snake[0]
    nx, ny = x+direction[d][0], y + direction[d][1]
    if 0 <= nx < N and 0 <= ny < N and not (nx, ny) in snake:
        snake.appendleft((nx, ny))
    else:
        print(t)
        break
    # 사과가 있는지 검사
    if snake[0] in apple:
        apple.remove(snake[0])
    else:
        snake.pop()
    # 머리 전환 여부 확인
    if command and command[0][0] == t:
        if command[0][1] == 'L':
            d = d - 1 if d > 0 else 3
        else:
            d = d + 1 if d < 3 else 0
        command.popleft()
    # 시간 증가
    t += 1

