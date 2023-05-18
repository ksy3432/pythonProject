def backtrack(n, m, seq):
    if len(seq) == m:
        print(' '.join(map(str, seq)))
        return

    for i in range(n):
        seq.append(i+1);
        backtrack(n,m,seq);
        seq.pop()

n, m = map(int, input().split())
seq = []
backtrack(n, m, seq)