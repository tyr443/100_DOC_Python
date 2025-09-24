word = input("Type a word or sentence: ").strip().lower()
count = 0
letter = input("The letter we are counting: ").strip().lower()
for ch in word:
    if ch == letter:
        count += 1

print(f"There are {count} occurances of the letter {letter} in your input.")
