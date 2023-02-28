"""s = [[0] * 15 for i in range(5)]

for i in range(5):
    s = list(input())

for j in range(15):
    for i in range(5):
        if s[i][j] != 0:
            print(s[i][j], end='')"""

s = [[0] * 15 for i in range(5)]

for i in range(5):
    a = (list(input()))
    for j in range(len(a)):
        s[i][j] = a[j]

for i in range(15):
    for j in range(5):
        if s[j][i] != 0:
            print(s[j][i], end='')

