def is_palindrome(string):
    if not string.isalpha():
        print("Invalid input. Please enter only letters.")
        return False
    reversed_string = string[::-1]
    return reversed_string == string


word = input("Enter a word: ")
if is_palindrome(word):
    print(f"The word {word} is palindrome")
else:
    print(f"The word {word} is not palindrome")
