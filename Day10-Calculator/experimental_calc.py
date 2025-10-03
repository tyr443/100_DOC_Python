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

operations = {1: add, 2: sub, 3: times, 4: div}


while True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Clear (reset to 0)\n6. Quit\n")
    print(f"Result: {current_result}\n")
    try:
        choice = int(input("Choice: "))
    except ValueError:
        print("Not a valid input")
        continue

    if choice == 5:
        current_result = 0
        continue
    elif choice > 5:
        print(f"Final Result: {current_result}")
        exit()

    while True:
        try:
            num = float(input("Enter number: "))
            break
        except ValueError:
            print("Not a valid input\n")

    if choice in operations:
        current_result = operations[choice](current_result, num)
