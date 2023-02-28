x = int(input())
count = 0

while(1):
    if(x / 3 > 0):
        x = x % 3
        count += 1
        print("1.count =",count)
        print("1.x =",x)
        continue
    elif(x / 2 > 0):
        x = x % 2
        count += 1
        print("2.count =", count)
        print("2.x =", x)
        continue
    elif(x != 1):
        x -= 1
        count += 1
        print("3.count =", count)
        print("3.x =", x)
        continue
    else:
        break
