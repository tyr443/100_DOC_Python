x = int(input("enter the start of your range: "))
y = int(input("enter the end of your range: ")) + 1


for i in range(x, y):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
