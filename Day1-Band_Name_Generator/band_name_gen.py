print(
    "Welcome to band name generator, using a true and tried formula I will create for you a band "
    "name."
)
city = input("\nWhat is the name of your home town or city?\n").strip()
pet = input("\nWhat was the name of your first pet?\n").strip()

if not city or not pet:
    print("You didn't enter anything")
else:
    print(f"\nYour band name is \"{city} {pet}\"\nRock on {city} {pet}!!")
