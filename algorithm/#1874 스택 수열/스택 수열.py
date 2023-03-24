n = int(input())
stack_array = []
s = []
val = 1
res = 0


def push(x):
    global val
    stack_array.append(x)


for i in range(n):
    find = int(input())

    while val <= find:
        push(val)
        s.append('+')
        val += 1

    if find == stack_array[-1]:
        stack_array.pop()
        s.append('-')

    else:
        res = 1

if res == 0:
    for i in s:
        print(i)
else:
    print('NO')