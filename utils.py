"""
Utility functions
Journey to the Mysterious Island

Contains reusable functions used throughout the game.
"""


def banner(title):
    """Display a formatted title banner."""

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def prompt_choice(question, options):
    """
    Ask the player to select one option.

    Input is case-insensitive and continues until
    the player enters a valid choice.
    """

    print(f"\n{question}")

    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    valid_options = [option.lower() for option in options]

    while True:
        answer = input("> ").strip().lower()

        # Allow the player to enter the option number.
        if answer.isdigit():
            number = int(answer)

            if 1 <= number <= len(options):
                return valid_options[number - 1]

        # Allow the player to type the full option.
        if answer in valid_options:
            return answer

        print("Please choose one of the available options.")


def checkpoint(label):
    """Return the checkpoint used by the main game loop."""

    return label


def restart_chapter(label):
    """Display a restart message and return a checkpoint."""

    print("\nRestarting...\n")
    return label
