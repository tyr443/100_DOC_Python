import random
import string

while True:
    pass_len = int(input("How many characters: "))  # Password length variable
    if pass_len < 9:
        print("Your password must be at least 9 characters long")
    else:
        break

letters = list(string.ascii_lowercase)  # All letters, lowercase
numbers = list(string.digits)  # Numbers 0 - 9
symbols = list("!@#$%")  # Symbols
password_chars = []  # Empty password list

# Force a single output from each of the lists, add to password list
password_chars.append(random.choice(numbers))
password_chars.append(random.choice(symbols))
password_chars.append(random.choice(letters))

all_chars = letters + numbers + symbols  # Combine all the characters

for i in range(pass_len - 3):  # remove the three forced characters from the length
    password_chars.append(random.choice(all_chars))  # Select random characters


random.shuffle(password_chars)  # Shuffle the entire list

password = "".join(password_chars)  # Turn list into a string

print(password)
