def apply_move(pos, move):
    x, y = pos
    m = move.lower()

    if m == "n":
        y = y - 1
    elif m == "s":
        y = y + 1
    elif m == "e":
        x = x + 1
    elif m == "w":
        x = x - 1

    return (x, y)


steps_taken = 0

player = (6, 6)  # Bottom right of a 7x7

blocked_edges = {
    frozenset({(3, 4), (3, 3)}),
    frozenset({(2, 3), (3, 3)}),
    frozenset({(4, 3), (3, 3)}),
    frozenset({(2, 2), (3, 2)}),
    frozenset({(2, 2), (2, 1)}),
    frozenset({(4, 2), (3, 2)}),
    frozenset({(4, 2), (4, 1)}),
    frozenset({(5, 2), (5, 1)}),
    frozenset({(6, 1), (5, 1)}),
    frozenset({(5, 0), (5, 1)}),
    frozenset({(4, 0), (4, 1)}),
    frozenset({(3, 0), (3, 1)}),
}

goal = (3, 3)

while player != goal:
    direction = input("Please enter n, s, e, w: ")
    if direction != "exit":
        movement = apply_move(player, direction)
    else:
        exit()

    if 0 <= movement[0] <= 6 and 0 <= movement[1] <= 6:
        if frozenset({player, movement}) in blocked_edges:
            print("The path is blocked!")
        else:
            player = movement
            print(player)
            steps_taken += 1

    else:
        print("cannot move any further in this direction")

print(f"You escaped in {steps_taken} steps!")
