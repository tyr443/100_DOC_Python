import string


def caesar_cipher(text, shift):
    lc_letters = string.ascii_lowercase
    uc_letters = string.ascii_uppercase
    shifted_text = []
    for ch in text:
        if ch not in lc_letters and ch not in uc_letters:
            shifted_text.append(ch)
            continue

        pos = lc_letters.index(ch.lower())
        new_pos = (pos + shift) % 26
        if ch in lc_letters:
            new_ch = lc_letters[new_pos]
        else:
            new_ch = uc_letters[new_pos]
        shifted_text.append(new_ch)
    return "".join(shifted_text)


phrase = input("Enter a word or phrase:\n")
while True:
    try:
        offset = int(input("Enter how many letters do you want to shift by: "))
        break
    except ValueError:
        print("Please enter a number for the offset")

cipher = caesar_cipher(phrase, offset)
print(cipher)
