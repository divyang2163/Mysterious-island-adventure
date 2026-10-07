"""
Chapter 5
The Nautilus and Escape
"""

from utils import banner, prompt_choice, checkpoint, restart_chapter


def play(state):
    """Run the final chapter of the adventure."""

    banner("Chapter 5: The Nautilus and Escape")

    print(
        "You and Grandpa enter the underground cavern."
    )

    print(
        "The Nautilus sits silently in the water while "
        "the volcano shakes the island around you."
    )

    # Open control panel
    choice = prompt_choice(
        "How will you open the submarine control panel?",
        [
            "Use Nautilus Key",
            "Bypass wiring manually",
            "Force panel open",
            "Wait for Grandpa"
        ]
    )

    if choice == "use nautilus key":

        if state.get("nautilus_key"):
            print(
                "\nThe key fits perfectly."
            )

            print(
                "The control panel unlocks."
            )

            state["panel_opened"] = True

        else:
            print(
                "\nYou do not have the required key."
            )

            return restart_chapter("CH5_SUB")

    elif choice == "bypass wiring manually":
        print(
            "\nYou carefully reconnect several damaged wires."
        )

        print(
            "Sparks fly, but the control panel opens."
        )

        state["panel_opened"] = True

    elif choice == "force panel open":
        print(
            "\nThe damaged mechanism jams completely."
        )

        return restart_chapter("CH5_SUB")

    else:
        print(
            "\nYou wait too long."
        )

        print(
            "Lava begins entering the cavern."
        )

        return restart_chapter("CH1")

    # Passphrase
    print(
        "\nInside the submarine, the control system activates."
    )

    print(
        "A mechanical voice says:"
        '\n"Enter activation phrase."'
    )

    choice = prompt_choice(
        "Which phrase will you use?",
        [
            "Heart of Fire",
            "Calm Seas",
            "Stay Silent"
        ]
    )

    if choice == "heart of fire":

        if state.get("passphrase") == "heart of fire":
            print(
                "\nThe engines roar to life!"
            )

            state["engines_on"] = True

        else:
            print(
                "\nThe system rejects the phrase."
            )

            return restart_chapter("CH1")

    elif choice == "calm seas":
        print(
            "\nIncorrect phrase."
        )

        print(
            "The submarine shuts down."
        )

        return restart_chapter("CH5_SUB")

    else:
        print(
            "\nThe system times out while the cavern begins collapsing."
        )

        return restart_chapter("CH1")

    # Escape
    print(
        "\nThe Nautilus begins moving."
    )

    print(
        "Behind you, the underground cavern starts collapsing."
    )

    choice = prompt_choice(
        "Which escape route will you take?",
        [
            "Sea Tunnel",
            "Vent Shaft",
            "Wait inside the bay"
        ]
    )

    if choice == "sea tunnel":
        print(
            "\nYou guide the Nautilus through a narrow underwater tunnel."
        )

        print(
            "Moments later, the submarine reaches the open ocean."
        )

        print(
            "\nBehind you, the mysterious island disappears "
            "beneath smoke and waves."
        )

        state["ending"] = "Perfect Escape through the Sea Tunnel"

        return checkpoint("END_SUCCESS")

    if choice == "vent shaft":
        print(
            "\nYou steer the Nautilus through an unstable volcanic passage."
        )

        print(
            "After a dangerous climb through steam and falling rock, "
            "the submarine reaches open water."
        )

        state["ending"] = "Dangerous Escape through the Vent Shaft"

        return checkpoint("END_SUCCESS")

    print(
        "\nYou hesitate for too long."
    )

    print(
        "The cavern collapses around the submarine."
    )

    return restart_chapter("CH1")
