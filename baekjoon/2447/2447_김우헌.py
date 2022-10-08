'''
baekjoon g5 별 찍기 - 10
https://www.acmicpc.net/problem/2447
'''

import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

N = int(input())
star = [['*' for _ in range(N)] for _ in range(N)]

def makepattern(star, N, row, col):
    length = N // 3
    x = row + length
    y = col + length
    for r in range(x, x+length):
        for c in range(y, y+length):
            star[r][c] = ' '
    if length != 1:
        for r in range(3):
            for c in range(3):
                if r == c == 1:
                    ...
                else:
                    makepattern(star, length, row + r*length, col + c*length)

makepattern(star, N, 0, 0)

for s in star:
    print(''.join(s))