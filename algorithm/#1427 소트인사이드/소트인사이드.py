import sys       #merge_sort

n = str(sys.stdin.readline())       #s[]에 원소 넣기
s = []

for i in range(0, len(n)-1):
    s.append(int(n[i]))


#s = [9,9,9,9,9,8,9,9,9]

def merge_sort(s):
    global res
    if len(s) <= 1:
        return s

    mid = len(s) // 2
    left = merge_sort(s[:mid])
    right = merge_sort(s[mid:])

    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res += left[i:]
    res += right[j:]
            
    return res


res = merge_sort(s)
for i in res:
    print(i, end='')