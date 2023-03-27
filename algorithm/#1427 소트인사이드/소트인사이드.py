import sys

#n = list(map(str, input().split()))
n = str(sys.stdin.readline())
s = []

for i in range(0, len(n)-1):
    s.append(int(n[i]))

s.sort(reverse=True)

for i in s:
    print(i, end='')