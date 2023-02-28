n, m = map(int, input().split(' '))
s = [str(i+1) for i in range(n)]
res = 0

for k in range(m):
    i, j = map(int, input().split())
    res = s[i-1]
    s[i-1] = s[j-1]
    s[j-1] = res

for k in range(n):
    print(s[k],end=' ')