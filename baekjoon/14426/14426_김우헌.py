import sys
from collections import defaultdict

input = sys.stdin.readline


N, M = map(int, input().split())

string_dict = defaultdict(list)
for _ in range(N):
    s = input().rstrip()
    string_dict[s[0]].append(s)

ans = 0
for _ in range(M):
    p = input().rstrip()
    for s in string_dict[p[0]]:
        if s[:len(p)] == p:
            ans += 1
            break
print(ans)
    