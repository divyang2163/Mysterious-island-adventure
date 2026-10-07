# Author: Divyang Parikh

"""
Main Program
Journey to the Mysterious Island

This module controls the overall game flow.

Responsibilities:
- Welcome the player.
- Store shared game state.
- Route the player between chapters.
- Handle restarts and successful completion.
"""

from utils import banner
from chapter_1 import play as chapter_1
from chapter_2 import play as chapter_2
from chapter_3 import play as chapter_3
from chapter_4 import play as chapter_4
from chapter_5 import play as chapter_5


def main():
    """Start and manage the text-adventure game."""

    banner("Welcome to Journey to the Mysterious Island")

    player_name = input("Enter your name: ").strip() or "Explorer"

    print(f"\nWelcome, {player_name}!")
    print("Your adventure begins now...\n")

    state = {
        "player_name": player_name
    }

    current_chapter = "CH1"

    chapters = {
        "CH1": chapter_1,
        "CH2_CRASH": chapter_2,
        "CH3_GRANDPA": chapter_3,
        "CH4_SEARCH": chapter_4,
        "CH5_SUB": chapter_5,
    }

    while True:

        if current_chapter == "END_SUCCESS":
            banner("🎉 CONGRATULATIONS 🎉")

            print(
                f"Well done, {player_name}! "
                "You and Grandpa escaped the island successfully!"
            )

            print(f"Ending: {state.get('ending', 'Successful Escape')}")
            print("\nThank you for playing Journey to the Mysterious Island!")

            break

        if current_chapter not in chapters:
            print("\nUnknown checkpoint detected.")
            print("Restarting the adventure...\n")

            state = {"player_name": player_name}
            current_chapter = "CH1"
            continue

        next_chapter = chapters[current_chapter](state)

        # A full restart clears previous game progress.
        if next_chapter == "CH1" and current_chapter != "CH1":
            state = {"player_name": player_name}

        current_chapter = next_chapter


if __name__ == "__main__":
    main()
