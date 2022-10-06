'''
baekjoon s1 연산자 끼워넣기
https://www.acmicpc.net/problem/14888
'''

import sys
from itertools import permutations

input = sys.stdin.readline

class calculator:
    def __init__(self,num):
        self.num = num

    def __add__(self, num):
        self.num += num

    def __sub__(self, num):
        self.num -= num

    def __mul__(self, num):
        self.num *= num

    def __floordiv__(self, num):
        if self.num < 0:
            self.num = -(-self.num // num)
        else:
            self.num //= num


N = int(input())
num = input().split()
temp = input().split()
oper = []

for i in ['+', '-', '*', '//']:
    t = temp.pop(0)
    oper += [i] * int(t)

answer_list = []
for oper_set in set(permutations(oper, len(oper))):
    formula = calculator(int(num[0]))
    for i in range(1, len(num)):
        eval(f"formula {oper_set[i-1]} int({num[i]})")
    answer_list.append(formula.num)

print(max(answer_list))
print(min(answer_list))

