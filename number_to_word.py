def valid_input(digit):
    while True:
        user_input = input(digit)
        if user_input.isdigit():
            number = int(user_input)
            if 0 <= number <= 99:
                return number
            else:
                print("Please enter a number between 0 to 99")
        else:
            print("The input should be an integer")


def num_to_word_converter(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
             "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n == 0:
        return "Zero"

    if n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n]
    elif 20 <= n < 100:
        ten_part = tens[n // 10]
        one_part = ones[n % 10]
        if one_part != "":
            return ten_part + "-" + one_part
        else:
            return ten_part


number = valid_input("Enter a number between 0 to 99: ")
print(f"{number} in word is {num_to_word_converter(number)}")
