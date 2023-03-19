import sys

N = int(sys.stdin.readline())
s = []
count = 0

def push(x):
    global count
    s.append(x)
    count += 1

def pop():
    global count
    if count != 0:
        count -= 1
        print(s.pop(0))
    else:
        print(-1)

def size():
    global count
    print(count)

def empty():
    global count
    if count == 0:
        print(1)
    else:
        print(0)

def front():
    if count != 0:
        print(s[0])
    else:
        print(-1)

def back():
    if count != 0:
        print(s[-1])
    else:
        print(-1)

for i in range(N):
    char_input = sys.stdin.readline().split()
    
    if char_input[0] == "push":
        push(int(char_input[1]))
    elif char_input[0] == "pop":
        pop()
    elif char_input[0] == "size":
        size()
    elif char_input[0] == "empty":
        empty()
    elif char_input[0] == "front":
        front()
    elif char_input[0] == "back":
        back()