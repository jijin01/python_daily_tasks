import random


def valid_input(digit):
    while True:
        try:
            user_input = input(digit)
            if user_input.isdigit():
                return user_input
        except ValueError:
            return "Enter a valid integer"


attempts = 3


def dice_game():
    global attempts
    print("Welcome to the Number Guessing Game!")
    dice_roll = random.randint(1, 6)

    while attempts > 0:
        guess = valid_input(" Guess a number between 1 to 6: ")
        if guess == dice_roll:
            print("Your guess is correct. You won")
            break

        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong guess, the answer is {dice_roll} .You have {attempts} attempts left ")


            else:
                print("Your attempts exceeded the limit, Game over")
                break


dice_game()
