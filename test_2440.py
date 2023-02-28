n = int(input())
result = "long int"

if n < 4:
    print(result)
else:
    n = (n - 4) // 4
    for i in range(0, n):
        print("long", end=" ")
    print("long int")