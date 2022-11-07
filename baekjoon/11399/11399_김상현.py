# 11399 ATM < 실버 4 >
from sys import stdin
N = int(stdin.readline())
P = sorted(list(map(int,stdin.readline().split())),reverse=True)
print(sum(list(P[i-1] * i for i in range(N,-1,-1))))