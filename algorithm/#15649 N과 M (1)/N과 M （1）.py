n, m = map(int, input().split())
s = []
number = [i + 1 for i in range(n)]
check = [False] * n

def backtrack():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(n):
        if not check[i]:
            check[i] = True
            s.append(number[i])
            backtrack()
            check[i] = False
            s.pop()

backtrack()