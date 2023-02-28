word = input()

if word[::-1] == word[::]:
    print("1\n")
else:
    print("0\n")