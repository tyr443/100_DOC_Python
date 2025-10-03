def add(a, b):
    return a + b


def times(a, b):
    return a * b


def sub(a, b):
    return a - b


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "You cannot divide by 0"


current_result = 0

print(f"Current result: {current_result}\n")


while True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Clear (reset to 0)\n6. Quit\n")
    try:
        choice = int(input("Choice: "))
    except ValueError:
        print("Not a valid input")
        continue

    if choice < 5:
        while True:
            try:
                num = float(input("Enter number: "))
                break
            except ValueError:
                print("Not a valid input\n")

    if choice == 1:
        current_result = add(current_result, num)
    elif choice == 2:
        current_result = sub(current_result, num)
    elif choice == 3:
        current_result = times(current_result, num)
    elif choice == 4:
        current_result = div(current_result, num)
    elif choice == 5:
        current_result = 0
    else:
        print(f"Final Result: {current_result}")
        exit()

    print(f"Result: {current_result}\n")
