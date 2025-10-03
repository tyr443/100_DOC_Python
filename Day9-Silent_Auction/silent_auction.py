auction = {}
winner = ""
highest_bid = 0

while True:
    name = input("Please enter your name: ")

    if name == "end":
        break

    while True:
        try:
            bid = round(float(input("Please enter your bid: ")), 2)
            break
        except ValueError:
            print("please enter a valid bid")

    auction[name] = bid

highest_bid = max(auction.values())
winners = [name for name, bid in auction.items() if bid == highest_bid]


if len(winners) == 1:
    print(f"The winner is {winners[0]} with a bid of €{highest_bid}")
else:
    print(f"The winners are {', '.join(winners)} with a bid of €{highest_bid}")
