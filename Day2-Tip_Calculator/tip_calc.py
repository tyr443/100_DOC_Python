total_bill = float(input("What is the total bill: €"))
no_people = int(input("How many people: "))
tip_percent = int(input("What percentage tip will you leave: "))

total_w_tip = round(total_bill * ((tip_percent / 100) + 1), 2)

print(f"The total bill including tip is €{total_w_tip:.2f}")

print(f"That is {total_w_tip / no_people:.2f} per person.")
