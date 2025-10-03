import datetime

diary = "diary.txt"
e = 0

with open(diary) as file:
    lines = file.readlines()
    for line in lines:
        if "Entry" in line:
            e += 1

while True:
    print("=== Menu ===\n1. Add entry\n2. View all entries\n3. Quit")
    mode = int(input("Mode: "))

    d = datetime.datetime.now()
    heading = d.strftime("%a %d %b %Y - %H:%M:%S")
    if mode == 1:
        e += 1
        with open(diary, "a") as file:
            entry = input("Entry: ")
            file.write(f"\n{heading}\n Entry {e}:\n{entry}")

    elif mode == 2:
        with open(diary) as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    else:
        exit()
