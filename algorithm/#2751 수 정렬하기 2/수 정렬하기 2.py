import sys

n = int(input())
s = [int(sys.stdin.readline()) for i in range(n)]

s.sort()

for i in s:
    print(i)