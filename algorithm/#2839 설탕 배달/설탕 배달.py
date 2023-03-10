n = int(input())
count,size = 0,0

if n % 5 == 0:
    count = n // 5
    print(int(count))

else:
    for i in range(n//3):
        n -= 3
        count += 1
        if n % 5 == 0:
            count += n // 5
            n = 0
            print(int(count))
            break
    if n != 0:
        print("-1\n")