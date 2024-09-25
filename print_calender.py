import calendar


def print_calendar(month, year):
    cal = calendar.TextCalendar()

    print(cal.formatmonth(year, month))


def valid_input(data):
    while True:
        user_input = input(data)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input")


month = valid_input("Enter a month: ")
year = valid_input("Enter a year: ")

print_calendar(month, year)
