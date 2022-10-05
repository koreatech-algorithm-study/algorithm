# 14888 연산자 끼워넣기 <실버 1 >
from sys import stdin, maxsize
from itertools import permutations

def calculator(num1,num2,operator):
    if operator == '+': return num1+num2
    if operator == '-': return num1-num2
    if operator == '*': return num1*num2
    if operator == '/': return int(num1/num2) # C++14의 기준

def solution(N,A,add,sub,mul,div):
    maxValue, minValue = -maxsize, maxsize # 최대값, 최소값
    operator = ['+'] * add + ['-'] * sub + ['*'] * mul + ['/'] * div # 연산자 목록

    print(operator)

    # 모든 연산 순열
    for expression in permutations(operator,N-1):
        # 연산식 계산
        num1 = A[0]
        for o, num2 in zip(expression,A[1:]):
            num1 = calculator(num1,num2,o)
        # 연산 결과값 최대, 최소 비교
        maxValue = max(maxValue, num1)
        minValue = min(minValue, num1)

    return maxValue, minValue

N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))
add, sub, mul, div = map(int,stdin.readline().split())

maxValue, minValue = solution(N,A,add,sub,mul,div)
print(maxValue)
print(minValue)