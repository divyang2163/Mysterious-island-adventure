"""
Chapter 1
The Message and the Flight
"""

from utils import banner, prompt_choice, checkpoint, restart_chapter


def play(state):
    """Run Chapter 1 of the adventure."""

    banner("Chapter 1: The Message and the Flight")

    player = state.get("player_name", "Explorer")

    print(
        f"{player} receives a mysterious coded message connected "
        "to a missing family member and an island hidden beyond a dangerous storm."
    )

    print(
        "\nTo reach the island, you must decode the message, "
        "find a pilot, and survive the flight."
    )

    # Decode the message
    choice = prompt_choice(
        "How will you decode the mysterious message?",
        [
            "Use frequency scanner",
            "Guess pattern",
            "Give up"
        ]
    )

    if choice == "use frequency scanner":
        print("\nYou decode the coordinates perfectly.")
        state["coords"] = True

    elif choice == "guess pattern":
        print(
            "\nYou manage to recover approximate coordinates, "
            "although some information is missing."
        )
        state["coords"] = False

    else:
        print("\nYou abandon the mission before it begins.")
        return restart_chapter("CH1")

    # Find a pilot
    choice = prompt_choice(
        "How will you convince a pilot to help you?",
        [
            "Offer payment and explain the plan",
            "Tell the pilot why the mission matters",
            "Give up looking"
        ]
    )

    if choice == "offer payment and explain the plan":
        print("\nThe pilot studies your plan and agrees to help.")
        state["pilot_help"] = True

    elif choice == "tell the pilot why the mission matters":
        print("\nYour story convinces the pilot to take the risk.")
        state["pilot_help"] = True

    else:
        print("\nWithout a pilot, you cannot reach the island.")
        return restart_chapter("CH1")

    # Storm
    print(
        "\nYou take off toward the coordinates. "
        "Soon, dark clouds surround the helicopter."
    )

    choice = prompt_choice(
        "A violent storm hits. What will you do?",
        [
            "Follow the pilot's instructions",
            "Panic and ignore directions"
        ]
    )

    if choice == "follow the pilot's instructions":
        print(
            "\nYou help the pilot control the helicopter, "
            "but lightning strikes nearby."
        )

        print(
            "The engine begins to fail as the mysterious island "
            "appears below."
        )

        print(
            "\nThe pilot makes an emergency landing. "
            "The helicopter crashes into the jungle, but you survive."
        )

        return checkpoint("CH2_CRASH")

    print("\nThe helicopter loses control and disappears into the storm.")
    return restart_chapter("CH1")
