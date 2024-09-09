def get_string(prompt):
    return input(prompt).strip()


def reverse_string(s):
    return s[::-1]


def main():
    print("Welcome to the String Reversal Program!")
    user_string = get_string("Enter a string to reverse: ")

    reversed_string = reverse_string(user_string)
    print(f"The reversed string is: {reversed_string}")


main()
