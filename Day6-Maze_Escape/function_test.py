def square(n):
    return n * n


x = 0
while x < 100:
    inp = int(input("What number would you like to square: "))

    if inp == 0:
        print("Thanks, bye!")
        exit()
    else:
        x = square(inp)
        print(x)
