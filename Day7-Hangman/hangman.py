import random

options = ["work", "sleep", "eat"]
word = random.choice(options)
hangman = []
letters = []
lives = 3

for i in range(len(word)):
    hangman.append("_")

while "_" in hangman and lives > 0:
    print(" ".join(hangman))
    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter (a–z).")
        continue

    if guess in letters:
        print("You have already guessed this letter")
        print(f"Guessed so far: {letters}")
        continue

    hit = False
    for i in range(len(word)):
        if word[i] == guess:
            hangman[i] = guess
            hit = True

    letters.append(guess)

    if not hit:
        lives -= 1
        print(f"You have {lives} lives remaining")

if lives != 0:
    print("Congratulations you win!")
    print(f"The word was {word}")
else:
    print(f"You lose, the word was {word}")
