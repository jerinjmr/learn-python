"""Main file."""
import sys
from guess_number import guess_game

if __name__ == '__main__':
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except (ValueError, IndexError):
        print("Invalid input. Existing program")
        sys.exit(0)
    print(guess_game(start, end))
