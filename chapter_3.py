"""
Chapter 3
Grandpa and the Hidden Clues
"""

from utils import banner, prompt_choice, checkpoint, restart_chapter


def play(state):
    """Run Chapter 3 of the adventure."""

    banner("Chapter 3: Grandpa and the Hidden Clues")

    player = state.get("player_name", "Explorer")

    print(
        "You follow the mountain trail until you reach "
        "a small hut hidden among the rocks."
    )

    print(
        "\nInside, you finally find Grandpa."
    )

    print(
        "He explains that the island is becoming unstable "
        "and could soon disappear beneath the ocean."
    )

    print(
        "\nYour only chance of escape is an old submarine "
        "hidden somewhere beneath the island."
    )

    print(
        "\nTo locate and activate it, you need three clues:"
    )

    print("- An activation phrase")
    print("- A map to the hidden bay")
    print("- A Nautilus key")

    locations = {
        "Beach Cave": False,
        "Old Outpost": False,
        "Forest Shrine": False
    }

    # Search all three clue locations.
    while not all(locations.values()):

        remaining = [
            location
            for location, visited in locations.items()
            if not visited
        ]

        choice = prompt_choice(
            "Where would you like to search next?",
            remaining
        )

        if choice == "beach cave":
            print(
                "\nYou crawl through a cave filled with glowing coral."
            )

            print(
                "At the end, you discover a brass plate engraved "
                "with the words: HEART OF FIRE."
            )

            state["passphrase"] = "heart of fire"
            locations["Beach Cave"] = True

        elif choice == "old outpost":
            print(
                "\nYou climb to an abandoned research outpost."
            )

            print(
                "Inside an old journal, you discover a map showing "
                "a route to a hidden volcanic bay."
            )

            state["map_to_bay"] = True
            locations["Old Outpost"] = True

        elif choice == "forest shrine":
            print(
                "\nDeep in the jungle, you discover an ancient stone shrine."
            )

            print(
                "Inside the statue's hands rests an old metal key "
                "marked with a submarine symbol."
            )

            state["nautilus_key"] = True
            locations["Forest Shrine"] = True

    print(
        "\nWith all three clues collected, "
        f"{player} begins the journey back toward Grandpa."
    )

    # Giant bird encounter
    print(
        "\nSuddenly, giant birds descend from the cliffs above!"
    )

    choice = prompt_choice(
        "How will you protect yourself?",
        [
            "Hide under tree roots",
            "Wave a torch",
            "Throw rocks"
        ]
    )

    if choice == "hide under tree roots":
        print(
            "\nYou remain completely still beneath the roots."
        )

        print(
            "After several tense moments, the birds fly away."
        )

    elif choice == "wave a torch":
        print(
            "\nThe fire and smoke scare the birds away."
        )

        print(
            "You lose some supplies during the escape."
        )

        state["lost_supplies"] = True

    else:
        print(
            "\nThe birds easily avoid the rocks and attack from above."
        )

        return restart_chapter("CH3_GRANDPA")

    print(
        "\nYou return to Grandpa with all three clues."
    )

    print(
        '"Excellent," he says. '
        '"Now we can find the submarine."'
    )

    return checkpoint("CH4_SEARCH")
