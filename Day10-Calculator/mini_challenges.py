def multiply(a, b):
    return a * b


answer = multiply(6, 7)


def get_grade(a):
    if a < 60:
        return "F"
    elif a < 70:
        return "D"
    elif a < 80:
        return "C"
    elif a < 90:
        return "B"
    else:
        return "A"


result = get_grade(85)

print(result)


def calculate_change(to_pay, paid):
    change = float(paid) - float(to_pay)
    return change


test1 = calculate_change(3.50, 5)
test2 = calculate_change(12.25, 20)

print(test1)
print(test2)
