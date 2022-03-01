"""Guess the random number."""
from random import randint


def guess_game(start, end):
    """Guess the number."""
    while True:
        try:
            guess = int(input("Guess the number:"))
            # Skips bandit scan using nosec comment
            # Standard pseudo-random generators are not suitable for
            # security/cryptographic purposes
            num = randint(start, end)  # nosec
            print(f'Random number: {num}')
            if num == guess:
                return "You guessed it right"
        except ValueError as err:
            print("Enter an integer value")
            return err
        else:
            print("Bad luck. Try again")
