"""
Chapter 2
Crash Landing and Giant Creatures
"""

from utils import banner, prompt_choice, checkpoint, restart_chapter


def play(state):
    """Run Chapter 2 of the adventure."""

    banner("Chapter 2: Crash Landing and Giant Creatures")

    print(
        "You wake beside the damaged helicopter."
    )

    print(
        "The island is unlike anything you have seen before: "
        "tiny animals wander through enormous plants while strange "
        "creatures move deeper in the jungle."
    )

    # Explore
    choice = prompt_choice(
        "What will you do first?",
        [
            "Explore carefully",
            "Wander carelessly",
            "Stay near the helicopter"
        ]
    )

    if choice == "explore carefully":
        print(
            "\nYou carefully search the area and find "
            "fresh water and edible fruit."
        )

        state["has_food"] = True

    elif choice == "wander carelessly":
        print(
            "\nYou move deeper into the jungle without watching "
            "your surroundings."
        )

        state["has_food"] = False

    else:
        print(
            "\nNight begins to fall near the wreckage."
            "\nSomething large moves through the trees."
        )

        return restart_chapter("CH2_CRASH")

    # Giant creature encounter
    print(
        "\nSuddenly, a giant lizard steps onto the trail "
        "and blocks your path."
    )

    choice = prompt_choice(
        "How will you react?",
        [
            "Fight",
            "Escape",
            "Distract"
        ]
    )

    if choice == "fight":
        print(
            "\nYou try to fight the creature, "
            "but it is far stronger than you expected."
        )

        return restart_chapter("CH2_CRASH")

    if choice == "escape":
        print(
            "\nYou sprint through the jungle and eventually "
            "lose the creature."
        )

        print(
            "Ahead, you notice smoke rising from a distant mountain."
        )

        return checkpoint("CH3_GRANDPA")

    print(
        "\nYou throw part of your food supply away from the trail."
    )

    print(
        "The creature follows it, giving you enough time to escape."
    )

    state["lost_supplies"] = True

    print(
        "\nFrom a nearby ridge, you notice a small hut "
        "near the mountain."
    )

    return checkpoint("CH3_GRANDPA")
