print(
    "You are walking down a long dark road and reach a fork in the road.\n"
    "On the left road you see a light at the end.\n"
    "On the right road you see nothing, but you think you can hear the sea on that side.\n"
)

choice_1 = input("Which road will you take? ").strip().lower()

if choice_1 == "left":
    print(
        "\nYou walk down the left road and reach an old bar. It seems empty,\n"
        "but as you get closer two men come bursting out of the bar brawling.\n"
        "After a few seconds they look at you.\n\n"
        "At this moment your legs take full control and you bolt, running as fast as you can\n"
        "down the side of the building. You see an alley on the left and a door on the right.\n"
    )
    choice_2 = input("Which way will you go? ").strip().lower()

    if choice_2 == "right":
        print(
            "\nYou smash the door open. A whole room of people turns around in shock.\n"
            "After a pause someone shouts \"Happy Birthday!!\" and they begin to surround you celebrating.\n"
            "You realise these are all your friends, and the two fighting outside are old friends\n"
            "who have had far too much to drink.\n\n"
            "You celebrate all night and the story ends happily.\n"
        )
    elif choice_2 == "left":
        print(
            "\nYou run full speed down the alley and suddenly hear someone shouting your name.\n"
            "It sounds like it is coming from behind. You slow to a stop and realise it is an old\n"
            "friend from school, he was the one fighting.\n\n"
            "After some explanation you are led to your, now not-so-surprise, birthday party.\n"
            "Your story ends happily.\n"
        )
    else:
        print(
            "\nYou make no clear decision. In your momentum and indecision you run full speed\n"
            "into the wall directly ahead of you.\n\n"
            "Months later you wake up in the hospital with the doctor explaining that you were\n"
            "in a coma. The people you were running from were two drunk friends, and there\n"
            "had been a surprise party planned. Now you only have years of rehab to look forward to.\n"
            "The end.\n"
        )

elif choice_1 == "right":
    print(
        "\nYou follow the road to the right. The further you walk, the more sand is under your feet.\n"
        "You continue until you reach some rocks. The water begins to worry you, so you decide to turn back.\n"
        "But it is too late — the tide has trapped you.\n\n"
        "You try to swim but are not a strong enough swimmer. You are found the next morning by a jogger,\n"
        "barely breathing. Looks like your story will end in the hospital.\n"
    )
else:
    print(
        "\nThat decision wasn't an option. In your indecisiveness you suddenly feel a warm energy,\n"
        "and a bright spotlight overhead turns on.\n\n"
        "The next thing you know you are floating. The next day you awake in some bushes\n"
        "in an unknown place, hearing what you believe to be Chinese, with a pain in your arse.\n"
        "Your story ends here.\n"
    )
