n = int(input())
s = []

"""
for i in range(0, n, 1):
    if i == 0:
        a = input()
        s.append(a)
        print(s)

    else:
        a = input()

        if a == '0':
             s.insert(i-1, '0')
             s.insert(i, '0')
             del s[i+1]
             print(s)

        else:
             s.append(a)
             print(s)"""

count = 0

for i in range(0, n):
    a = input()
    s.append(a)
    count += 1
    #print(s)

    if a == '0':
        for j in range(count-1, -1, -1):
            if s[j] != '0':
                #print("반복 확인용 : ", j)
                s[j] = '0'
                #print(s)
                if(j != 0):
                    break;
                else:
                    s[j] = '0'

s = map(int, s)
print(sum(s))
