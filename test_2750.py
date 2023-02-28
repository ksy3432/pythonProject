n = int(input())
s = []

for i in range(n):
    a = int(input())
    s.append(a)

print("원래 배열 :",s)

"""min = 1

for i in range(len(s), -1, -1):
    print("i =",i)
    #if(s[i] < min):
        #min = s[i]
    s.insert(i, s[i])
    print(s)"""

s.sort()
print(s)