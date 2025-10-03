# while True:
#     try:
#         a = float(input("a: "))
#         b = float(input("b: "))
#         c = a / b
#         break
#     except ValueError:
#         print("invalid input")
#     except ZeroDivisionError:
#         print("Cannot divide by 0")

# print(c)


# def safe_read_file(filename):
#     try:
#         with open(filename) as file:
#             return file.read()
#     except FileNotFoundError:
#         return None


def get_positive_number():
    while True:
        try:
            a = int(input("a = "))
            if a > 0:
                return a
            else:
                print("must be a positive non-zero number")

        except ValueError:
            print("not a number")


get_positive_number()
