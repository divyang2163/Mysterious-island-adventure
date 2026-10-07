"""
Chapter 4
Searching for the Submarine Bay
"""

from utils import banner, prompt_choice, checkpoint, restart_chapter


def play(state):
    """Run Chapter 4 of the adventure."""

    banner("Chapter 4: Searching for the Submarine Bay")

    player = state.get("player_name", "Explorer")

    print(
        "You and Grandpa travel toward the volcanic center "
        "of the island."
    )

    print(
        "Steam rises from cracks in the ground while "
        "small earthquakes shake the mountain."
    )

    print(
        f'\nGrandpa warns, "{player}, the island is breaking apart. '
        'We need to move quickly."'
    )

    route = prompt_choice(
        "Which route will you take?",
        [
            "Ridge Path",
            "Tide Pools",
            "Lava Tubes",
            "Stay at camp"
        ]
    )

    if route == "ridge path":
        print(
            "\nYou climb above the jungle and discover "
            "steam vents leading toward the volcano."
        )

        state["vents_marker"] = True

    elif route == "tide pools":
        print(
            "\nYou follow the coastline and discover "
            "a hidden water tunnel leading inland."
        )

        state["secret_water_entry"] = True

    elif route == "lava tubes":
        print(
            "\nYou crawl through old lava tunnels beneath the mountain."
        )

        print(
            "Metal rails along the floor suggest that machinery "
            "once traveled through them."
        )

        state["mechanical_track"] = True

    else:
        print(
            "\nYou wait too long."
        )

        print(
            "The volcano erupts and blocks every route forward."
        )

        return restart_chapter("CH1")

    # Verify clues from previous chapter.
    required_clues = (
        state.get("passphrase"),
        state.get("map_to_bay"),
        state.get("nautilus_key")
    )

    if not all(required_clues):
        print(
            "\nYou do not have enough information to locate the submarine."
        )

        return restart_chapter("CH3_GRANDPA")

    print(
        "\nUsing the map and your route markers, "
        "you navigate through the mountain."
    )

    print(
        "\nA huge underground cavern finally appears."
    )

    print(
        "Floating in the glowing water is an enormous "
        "metal submarine."
    )

    print(
        '\nGrandpa whispers, "We found the Nautilus."'
    )

    return checkpoint("CH5_SUB")
