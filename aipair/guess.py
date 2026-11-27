import random


def play_game():
    number = random.randint(1, 15)
    attempts = 3

    print("Guess the number between 1 and 15.")

    while attempts > 0:
        try:
            guess = int(input(f"Enter your guess ({attempts} attempts left): "))
        except ValueError:
            print("Invalid input. Please enter a whole number between 1 and 15.")
            continue

        if not 1 <= guess <= 15:
            print("Invalid input. Please enter a number between 1 and 15.")
            continue

        attempts -= 1

        if guess == number:
            print("Correct! You guessed the number.")
            return
        if guess < number:
            print("Too low. Try a higher number.")
        else:
            print("Too high. Try a lower number.")

    print(f"Out of attempts. The number was {number}.")


if __name__ == "__main__":
    play_game()