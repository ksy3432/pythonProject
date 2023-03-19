n = int(input())
a = [int(x) for x in input().split()]

m = int(input())
b = [int(x) for x in input().split()]

a.sort()

for find in b:
    low = 0
    high = len(a) - 1
    found = False
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == find:
            found = True
            break
        elif a[mid] < find:
            low = mid + 1
        else:
            high = mid - 1
    if found:
        print(1)
    else:
        print(0)
        
