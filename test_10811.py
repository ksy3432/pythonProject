n, m = map(int, input().split())
s = [str(i+1) for i in range(n)]

for l in range(m):
    i, j = map(int, input().split())
    s = s[0:i-1] + s[i-1:j][::-1] + s[j:]

print(" ".join(str(k) for k in s))
