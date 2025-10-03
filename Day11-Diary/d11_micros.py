# print("r Read\nw Write\na Ammend\nq Quit")
# while True:
#     option = input("Select and option: ").lower()
#     if option == "q":
#         exit()

#     with open("log.txt", option) as file:
#         if option == "r":
#             content = file.read()
#             print(content)
#         else:
#             log = input("Type: ")
#             file.write(log)


with open("numbers.txt", "w") as file:
    file.write("10\n20\n30\n40")

with open("numbers.txt") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
