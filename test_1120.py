a, b = map(list, input().split())
n = len(b) - len(a)
count = [0]*(n+1)

for m in range(0, n+1):
    for i in range(0, len(a)):
           if(b[m+i] != a[i]):
               count[m] += 1

print(min(count))