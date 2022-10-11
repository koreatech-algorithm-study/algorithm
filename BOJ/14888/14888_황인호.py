'''
https://www.acmicpc.net/problem/14888
'''
from itertools import permutations

n = int(input())
num = list(map(int, input().split(' ')))
tmp = list(map(int, input().split(' ')))
oper = []
[[oper.extend([i]) for j in range(tmp[i])] for i in range(len(tmp))]

def operate_put(n, num, oper):
    permut = set(permutations(oper))
    maxi = -100000000
    mini = 100000000

    for o in permut:
        tmp = num[0]
        for i in range(n-1):
            if o[i] == 0: tmp += num[i + 1]
            elif o[i] == 1: tmp -= num[i + 1]
            elif o[i] == 2: tmp *= num[i + 1]
            elif o[i] == 3: tmp = int(tmp / num[i + 1])
        if tmp > maxi:
            maxi = tmp
        if tmp < mini:
            mini = tmp
    return maxi, mini

a, b = operate_put(n, num, oper)
print(a)
print(b)