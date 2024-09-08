import random


def get_guess(number):
    while True:
        try:
            guess = int(input(number).strip())
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def guess_the_number():
    print("Welcome to the Guess the Number Game!")

    random_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 3

    while True:
        guess = get_guess("Enter your guess (between 1 and 100): ")
        attempts += 1

        if attempts == max_attempts and guess != random_number:
            print(f"Your attempts have exceeded the limit. The correct number was {random_number}.")
            break

        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {random_number} in {attempts} attempts.")
            break


guess_the_number()
