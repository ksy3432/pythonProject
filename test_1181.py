n = int(input())
s = []

for i in range(n):
    s.append(input())

s.sort()
s.sort(key=len)

res = dict.fromkeys(s)
res2 = list(res)

for i in range(len(res2)):
    print(res2[i])

"""
for i in range(0, s):
    for j in range(0, len(s[i]))
       if s[][] == s[i][j+1]:
        del s[i+1]"""

"""for i in list(s):
    if(len(s[i]) > len(s[i+1])):
        s.insert(s[i+1],s[i])

print(s)"""
