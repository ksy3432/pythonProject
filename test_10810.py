n, m = map(int,input().split())
s = [0]*n

for u in range(m):
     i,j,k = map(int,input().split())
     for l in range(i, j+1, 1):
         s[l-1] = k

for t in range(n):
     print(s[t],'', end='')





