def get_year(value):
    while True:
        try:
            year = int(input(value).strip())
            if year < 0:
                print("Please enter a valid positive integer for the year.")
            else:
                return year
        except ValueError:
            print("Invalid input. Please enter a valid year.")


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def main():
    print("Welcome to the Leap Year Checker!")

    year = get_year("Enter a year to check if it is a leap year: ")

    if is_leap_year(year):
        print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year.")


main()
