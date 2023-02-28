n, k = map(int, input().split())
s = []
count = 0

for i in range(1, n+1):
    if n % i == 0:
        s.append(i)
        count += 1

if(k > len(s)):
    print(0)
else:
    print(s[k-1])